from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("",views.ProjectsViewSetApiView)

urlpatterns = [
    path('',include(router.urls)),
    path('users/',views.UsersGenericApiView.as_view()),
]
