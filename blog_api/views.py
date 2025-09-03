from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()   #custom postobjects manager
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostUserWritePermission(BasePermission):
    """
    Object-level permission to only allow author of an object to edit it, others can only read.
    """
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [PostUserWritePermission]  #using custom permission class



"""
Concrete View Classes (DRF)
--------------------------------------------
CreateAPIView
? Used for create-only endpoints.

ListAPIView
? Used for read-only endpoints to represent a collection of model instances.

RetrieveAPIView
? Used for read-only endpoints to represent a single model instance.

DestroyAPIView
? Used for delete-only endpoints for a single model instance.

UpdateAPIView
? Used for update-only endpoints for a single model instance.

!Combined Generic Views
ListCreateAPIView
? Used for read-write endpoints to represent a collection of model instances.

RetrieveUpdateAPIView
? Used for read or update endpoints to represent a single model instance.

RetrieveDestroyAPIView
? Used for read or delete endpoints to represent a single model instance.

RetrieveUpdateDestroyAPIView
? Used for read-write-delete endpoints to represent a single model instance.

"""