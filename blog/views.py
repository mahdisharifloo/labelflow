from .models import BlogCard
from .serializers import BlogCardSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class BlogCardViewSetApiView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = BlogCard.objects.all()
    serializer_class = BlogCardSerializer
