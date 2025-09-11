from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny, BasePermission,IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters
from rest_framework.parsers import MultiPartParser, FormParser


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
    # permission_classes = [IsAuthenticated] 

    #? Basic filter
    # def get_queryset(self):
    #     user = self.request.user   #user have to be authenticated(logged in)
    #     return Post.objects.filter(author=user) #lists only posts created by the user(author)
    
    #returns a list of all posts for the user as filtered by username portion of URL
    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.filter(username=username)

    #? Filter against the URL(ID) , get post based on title/ slug(string)
    # def get_queryset(self):
    #     slug = self.kwargs.get('pk')
    #     print(slug)
    #     return Post.objects.filter(id=slug)  #use int for id
    #     # return Post.objects.filter(slug=slug)  #In urls.py ,use str for slug

    #?Filter against query parameter:
    def get_queryset(self):
        queryset = Post.objects.all()   
        #look in URL for `?username=adra` , DRF puts these in `self.request.query_params` 
        username = self.request.query_params.get('username')  
        if username is not None:     
            queryset = queryset.filter(username=username)
        return queryset

class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    # queryset = Post.postobjects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return Post.postobjects.get(slug=item)
    
    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug', None)
    #     print(slug)
    #     return Post.objects.filter(slug=slug)


#! DRF Filtering => Post Search - DjangoFilterBackend & SearchFilter & OrderingFilter
class PostListDetailFilter(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    #DajngoFilterBackend - get all post by adra '/api/posts/?author=adra'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['slug', 'author', ]

    #SearchFilter - get all posts mentioning "django" or "api" - '/api/posts/?search=django api'
    filter_backends = [filters.SearchFilter]
    search_fields = ['=slug']

    """
    '^' : starts-with search
    '=' : exact matches
    '@' : full text search (only in postgres db)
    '$' : regex search
    """

    #OrderingFilter - order posts by category - '/api/posts/?ordering=category'
    filter_backends = [filters.OrderingFilter]  
    ordering_fields = ['status', 'author']  #only sort by these, crucial for security
    ordering = ['-category']  #sets deafult sorting order - deafult to newest first

#! Combining all 
    # show all published posts by adra that mention 'REST', sort them by category.
    #@note /api/posts/?status=published&author=adra&search=REST&ordering=category
    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'author', ]
    search_fields = ['title', 'content',]
    ordering_fields = ['status', 'author', ]

#! Custom generic filtering
class IsAuthorFilterBackend(filters.BaseFilterBackend):
    #filter that allows users to see thier own stuff, add this to filter_backends list in view class, so that no need to write get_queryset in all different views
    def filter_queryset(self, request, queryset):
        return queryset.filter(author=request.user)


#! CRUD
# class PostCreate(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.postobjects.all()

#! Upload Image
class AdminFileUpload(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#view to collect the data before edit
class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()

#view to edit the post
class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()

#view to delete the post
class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()






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
