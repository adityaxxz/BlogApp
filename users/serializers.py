from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=3, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password', 'first_name')
        #write_only fields- for fields that should accept as input but never sent back to user 
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            
        instance.save()
        return instance