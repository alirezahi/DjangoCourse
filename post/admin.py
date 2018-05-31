from django.contrib import admin
from post.models import Post,Author,Tag
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name','name_created_date')

	fields = ('name',)

	list_filter = ('name','created_date')

	search_fields = ['name','created_date']

	readonly_fields = ('created_date',)

	empty_value_display = 'This Field is not Completed'

	def name_created_date(self,obj):
		return obj.name[:2] + ' ' + str(obj.created_date)


admin.site.register(Post)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)