from rest_framework import serializers
from django.conf import settings
from blog.models import Post, Category

#? Serializers for Category, User model to show Nested Objects in JSON response
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=settings.AUTH_USER_MODEL
        fields = ['id','username','firstname']
""" Using this response will be 
{
    ...
    "author": {
        "id": 5,
        "username": "jane_doe",
        "first_name": "Jane"
    },
    "category": {
        "id": 2,
        "name": "Programming"
    },
    ...
}
"""


class PostSerializer(serializers.ModelSerializer):
   #! Nested Objects - overriding default fields for author & category 
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title','image','slug', 'author', 'excerpt', 'content', 'status', 'category')

    #! Custom Validation
    #! Field-level validation - validates a single field
    def validate_title(self, value):
        #check if the title is not a forbidden word
        if "hitler" in value.lower():
            raise serializers.ValidationError("Title cnt contain hitler")
        return value
    
    #! Object-level validation - validates multiple fields
    def validate(self, data):
        #to check excerpt must be shorter than content else validationerror
        if 'excerpt' in data and 'content' in data:
            if data['excerpt'] and len(data['excerpt']) > len(data['content']):
                raise serializers.ValidationError("excerpt cnt be longer than content")
        return data



class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=3, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'username', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
