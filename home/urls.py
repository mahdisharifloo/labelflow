from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page),
    path('doc',views.HomePageAPIView.as_view())
]
