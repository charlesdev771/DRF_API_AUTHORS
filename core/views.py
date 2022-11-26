from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import generics 
from core.models import Authors
from core.serializers import AuthorsSerializer


class Create_And_View(generics.ListCreateAPIView):
    
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    

class UpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    
