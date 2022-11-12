from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from .models import Books
from .serializers import BooksSerializer

# Create your views here.

# trying out ListCreateAPIView for books >>>>
#this is now superfluous, but keeping it to check out in Insomnia:
class BooksList(generics.ListCreateAPIView):
    #overriding defaults, I think? setting some class attributes:
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data)
    # def book_list(self, request):
    #     return self.get_queryset()

    # def perform_create(self, serializer):
    #     serializer.save()

