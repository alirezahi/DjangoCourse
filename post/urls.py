from django.conf.urls import url
from post.views import sth as another_sth
from post.views import return_static_file

urlpatterns = [
    url(r'^hello/',another_sth,name='sth_function'),
    url(r'^index/',return_static_file)
]
