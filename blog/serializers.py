from rest_framework import serializers
from .models import BlogCard
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogCard
        fields = "__all__"


