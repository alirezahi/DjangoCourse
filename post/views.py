from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post,Author,Tag
from django.shortcuts import render_to_response
import jdatetime
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