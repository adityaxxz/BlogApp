from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#! view/object level permission
class PostUserWritePermission(BasePermission):
    #Object-level permission to only allow author of an object to edit it, others can only read.
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user 
    

#! Generic Views
class PostList(generics.ListAPIView):
    queryset = Post.postobjects.all()   #custom postobjects manager
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    #? Basic filter
    # def get_queryset(self):
    #     user = self.request.user   #user have to be authenticated(logged in)
    #     return Post.objects.filter(author=user) #lists only posts created by the user(author)

    #? Filter against the URL(ID) , get post based on title/ slug(string)
    # def get_queryset(self):
    #     slug = self.kwargs.get('pk')
    #     print(slug)
    #     return Post.objects.filter(slug=slug)  #In urls.py ,use str for slug
        # return Post.objects.filter(id=slug)  #use int for id

class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()
    
    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug', None)
    #     print(slug)
    #     return Post.objects.filter(slug=slug)


class PostListDetailFilter(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['slug']

    #SearchFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['=slug']

    """
    '^' : starts-with search
    '=' : exact matches
    '@' : full text search (only in postgres db)
    '$' : regex search
    """



# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     serializer_class = PostSerializer
#     permission_classes = [PostUserWritePermission]  #using custom permission class

#     queryset = Post.postobjects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return Post.postobjects.get(pk=item)
    
#     def get_queryset(self):
#         return Post.postobjects.all()



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

    






