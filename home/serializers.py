from rest_framework import serializers
from blog.models import BlogCard
from blog.serializers import BlogCardSerializer
from projects.models import Project
from django.contrib.auth import get_user_model
from projects.serializers import ProjectSerializer, UserSerializer


User = get_user_model()

class HomePageSerializer(serializers.Serializer):
    blog_card = serializers.SerializerMethodField(read_only=True)
    project = serializers.SerializerMethodField(read_only=True)
    rank_users = serializers.SerializerMethodField(read_only=True)

    def get_blog_card(self, obj):
        blogs = BlogCard.objects.all()
        serialized_blogs = BlogCardSerializer(blogs, many=True).data
        return serialized_blogs

    def get_rank_users(self,obj):
        users = User.objects.all()
        serialized_users = RankedUserSerializer(users,many=True).data
        return serialized_users

    def get_project(self, obj):
        projects = Project.objects.all()
        serialized_projects = ProjectSerializer(projects, many=True).data
        return serialized_projects

class RankedUserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = ['username', 'projects']