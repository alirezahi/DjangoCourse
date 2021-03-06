from django.db import models
from django.contrib.auth.models import User

tag_names = {
	'python':'پایتون',
	'programming':'برنامه نویسی'
}

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



class Tag(models.Model):
	name = models.CharField(max_length=50)


class Post(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(Author,on_delete='CASCADE')
	text = models.TextField()
	tags = models.ManyToManyField(Tag,related_name='posts')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']




