from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    def setUp(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser = User.objects.create_user(
            username='test_user',
            password='123'
        )
        # Create a test post
        Post.objects.create(
            title='Test Post',
            author=self.testuser,
            excerpt='Test excerpt',
            content='Test content',
            category=self.test_category,
            status='published',
            slug='test-post'
        )

    #test to see if we can view posts, access the data thru api
    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test to see if we can create data for our api
    def test_create_post(self):
        # Authenticate the user for creating posts
        self.client.force_authenticate(user=self.testuser)
        
        data = {
            "title": "New Post",
            "author": self.testuser.id,
            "excerpt": "New excerpt",
            "content": "New content",
            "category": self.test_category.id,
            "status": "published",
            "slug": "new-post"
        }

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_post_update(self):
        # Create a test post using the user from setUp
        test_post = Post.objects.create(
            category=self.test_category,
            author=self.testuser,
            title='Test Post for Update',
            excerpt='Test excerpt',
            content='Test content',
            status='published'
        )

        # Authenticate as the author of the post
        self.client.force_authenticate(user=self.testuser)

        url = reverse('blog_api:detailcreate', kwargs={'pk': test_post.pk})

        response = self.client.put(
            url, {
                "title": "Updated title",
                "author": self.testuser.id,
                "excerpt": "Updated excerpt",
                "content": "Updated content",
                "status": "published",
                "category": self.test_category.id,
            },
            format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)