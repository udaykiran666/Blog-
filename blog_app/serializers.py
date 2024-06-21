from django.contrib.auth.models import User
from django.forms import ValidationError
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uuid', 'name', 'created_at', 'updated_at')
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('uuid', 'description', 'created_at', 'updated_at', 'user')

    def get_user(self, obj):
        return obj.user.username if obj.user else None

    def create(self, validated_data):
        blog = self.context.get('blog')
        if not blog:
            raise serializers.ValidationError("Blog is required.")
        
        validated_data['user'] = self.context['request'].user
        return Comment.objects.create(blog=blog, **validated_data)
class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    written_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Blog
        fields = ['uuid', 'title', 'description', 'written_by', 'categories', 'comments']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        blog = Blog.objects.create(**validated_data)       
        for category_data in categories_data:
            category_name = category_data.get('name')
            category = Category.objects.get(name=category_name)
            blog.categories.add(category) 
        return blog