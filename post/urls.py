from django.conf.urls import url
from post.views import sth as another_sth
from post.views import *

urlpatterns = [
    url(r'^hello/',another_sth,name='sth_function'),
    url(r'^index/',return_static_file),
    url(r'^author/',return_author_file,name='some_url'),
    url(r'^author_json/',author_json),
    url(r'^author_serializer/',author_serializer),
    url(r'^post_serializer/',post_serializer),
    url(r'^login/',login_users),

]
