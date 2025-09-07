from django.urls import path, include
from .views import PostList, PostDetail, PostListViewSet, PostListDetailFilter
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostListViewSet, basename='post')
# urlpatterns = router.urls



urlpatterns = [
    # API endpoints
    path('', PostList.as_view(), name='listcreate'),  #show all posts
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #show individual post

    # path('', include(urlpatterns)),

    # path('posts/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('posts/<int:pk>/', PostDetail.as_view(), name='detailcreate'),#based on id

    path('posts/', PostDetail.as_view(), name='detailcreate'), 

    path('search/', PostListDetailFilter.as_view(), name='search'),
]