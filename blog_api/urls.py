from django.urls import path, include
from .views import PostList, PostDetail, PostListViewSet, PostListDetailFilter, AdminFileUpload, EditPost, DeletePost, AdminPostDetail
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostListViewSet, basename='post')
# urlpatterns = router.urls



# API endpoints
urlpatterns = [
    path('', PostList.as_view(), name='listcreate'),  #show all posts
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #show individual post

    # path('', include(urlpatterns)),

    path('posts/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('posts/<int:pk>/', PostDetail.as_view(), name='detailcreate'),#based on id

    # path('posts/', PostDetail.as_view(), name='detailcreate'), 

    path('search/', PostListDetailFilter.as_view(), name='search'),

    path('admin/create/', AdminFileUpload.as_view(), name='createpost'),
    path('admin/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]