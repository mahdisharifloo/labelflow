from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("",views.BlogCardViewSetApiView)

urlpatterns = [
    path('cards/',include(router.urls)),
]
