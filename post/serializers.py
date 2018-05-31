from .models import Author,Tag,Post
from rest_framework import serializers
from rest_framework import permissions

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		exclude = ('id',)

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'

class AuthorCompleteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	author = AuthorSerializer()
	tags = TagSerializer(many=True)
	class Meta:
		model = Post
		fields = '__all__'


