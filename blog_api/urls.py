from django.urls import path, include
from .views import PostListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostListViewSet, basename='post')

urlpatterns = router.urls


# urlpatterns = [
#     # API endpoints
#     path('', PostList.as_view(), name='listcreate'),  #show all posts
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #show individual post

#     path('', include(urlpatterns)),
# ]