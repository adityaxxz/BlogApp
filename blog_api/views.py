from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response


#! view/object level permission
class PostUserWritePermission(BasePermission):
    #Object-level permission to only allow author of an object to edit it, others can only read.
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user 
    

#! Generic Views
"""
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()   #custom postobjects manager
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [PostUserWritePermission]  #using custom permission class
"""

#! ViewSets
# class PostListViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer = PostSerializer(self.queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         post = Post.postobjects.get(pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#! ModelViewSet
class PostListViewSet(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer

    lookup_field = 'slug'

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return Post.postobjects.get(slug=item)

    def get_queryset(self):
        return Post.postobjects.all()

    






