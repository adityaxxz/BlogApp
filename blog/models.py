from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

# Create your models here.

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Post (models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            #show only published posts, if status is published then return only published
            return super().get_queryset().filter(status='published')

    STATUS_CHOICES = [('draft', 'Draft'),('published', 'Published'),]

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    content = models.TextField()

    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    slug = models.SlugField(max_length=200, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager

    class Meta:
        ordering = ('-published',) # -published means descending order

    def __str__(self):
        return self.title