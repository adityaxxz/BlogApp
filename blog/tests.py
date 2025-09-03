from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

# Create your tests here.

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser = User.objects.create_user(
            username='testuser', 
            password='123'
        )
        testpost = Post.objects.create(
            title='post title',
            author=testuser,
            excerpt='test excerpt',
            category=test_category,
            status='published',
            content='test content',
            slug='post-slug',
        )

    def test_blog_content(self):
            post = Post.postobjects.get(id=1)
            category = Category.objects.get(id=1)
            author = f'{post.author}'
            title = f'{post.title}'
            excerpt = f'{post.excerpt}'
            content = f'{post.content}'
            status = f'{post.status}'

            self.assertEqual(author, 'testuser')
            self.assertEqual(content, 'test content')
            self.assertEqual(excerpt, 'test excerpt')
            self.assertEqual(status, 'published')
            self.assertEqual(title, 'post title')

            self.assertEqual(str(category), 'django')
            self.assertEqual(str(post), 'post title')