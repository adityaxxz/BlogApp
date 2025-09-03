from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    # API endpoints
    path('', PostList.as_view(), name='listcreate'),  #show all posts
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #show individual post
]