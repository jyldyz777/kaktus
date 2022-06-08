from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from News.models import News, Comment, Category
from News.serializers import NewsSerializer, CommentSerializer, CategorySerializer


class NewsAPIViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer