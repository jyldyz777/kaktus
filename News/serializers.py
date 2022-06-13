from rest_framework.serializers import ModelSerializer

from News.models import News, Comment, Category


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
