from rest_framework import serializers
from .models import BlogArticle
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta :
        model = BlogArticle 
        fields = ["id","title","description"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
