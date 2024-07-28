from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import HomePageSerializer





class HomePageAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        serializer = HomePageSerializer(data={})
        serializer.is_valid()
        return Response(serializer.data)
    

def index_page(request):
    context = {}
    return render(request,"home/index.html",context)
