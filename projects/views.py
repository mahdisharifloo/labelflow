
from .models import Project
from .serializers import ProjectSerializer,UserSerializer
from rest_framework import generics 
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrLabelerUser,IsAdminOrOrganizationUser


User = get_user_model()


#region  viewset


class ProjectsViewSetApiView(viewsets.ModelViewSet):
    queryset = Project.objects.order_by('priority').all()
    serializer_class = ProjectSerializer
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminOrOrganizationUser]
        elif self.action == 'list':
            permission_classes = [IsAdminOrLabelerUser,IsAdminOrOrganizationUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]


#endregion

#region users
class UsersGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

#endregion

