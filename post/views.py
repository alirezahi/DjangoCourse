from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post,Author,Tag
from django.shortcuts import render_to_response, render
from django.http import JsonResponse
from .serializers import AuthorSerializer,PostSerializer
from rest_framework.response import Response
import jdatetime
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate

# Create your views here.

def sth(request):
	my_time = jdatetime.datetime(1397,1,1,13,10,10)
	print(my_time)
	print(request)
	print(request.GET)
	print(request.user)
	# if request.user.username != 'admin':
	# 	return HttpResponse('WOW. not welcome')
	response = ''
	for post in Post.objects.filter(author__name='alireza'):
		response += str(my_time.date())
		response += '<h1>' + post.title + '</h1>' + '<div>' + post.text+'</div>'
		for tag in post.tags.all():
			response += '<div style="color:red">'+tag.name+'</div>'
		response += '<div style="height:100px"></div>'
	for tag in Tag.objects.all():
		response += '<br>'+tag.name
	print(response)
	return HttpResponse(response,status=200)

def return_static_file(request):
	posts = Post.objects.filter(author__name='alireza')
	authors = Author.objects.all()
	return render(request,'posts.html',{
		'posts':posts,
		'authors':authors,
		'dictionary':{
			'GOT':{
				'rate':8.9
			},
			'Westworld':{
				'rate':9
			},
			'Breaking Bad':{
				'rate':7
			}
		}
	})


def return_author_file(request):
	posts = Post.objects.filter(author__name='alireza')
	authors = Author.objects.all()
	return render(request,'author.html',{
		'posts':posts,
		'authors':authors,
		'ramadan':'We are starving',
		'wow':'Wooow'
	})

def author_json(request):
	authors = Author.objects.all()
	current_author = {}
	for author in authors:
		current_author = {}
		current_author['name'] = author.name
		current_author['created_date'] = author.created_date
	return JsonResponse(current_author)

@api_view(['GET','POST'])
def author_serializer(request):
	if request.method == 'GET':
		authors = Author.objects.all()
		author_serializers = AuthorSerializer(authors, many=True)
		return Response(author_serializers.data)
	if request.method == 'POST':
		author_serializer_create = AuthorSerializer(data=request.data)
		if author_serializer_create.is_valid():
			author_serializer_create.save()
		return Response(author_serializer_create.data)

@api_view(['GET','POST'])
def post_serializer(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		posts_serializers = PostSerializer(posts, many=True)
		return Response(posts_serializers.data)

@csrf_exempt
def login_users(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user:
			login(request,user)
	return HttpResponse('')