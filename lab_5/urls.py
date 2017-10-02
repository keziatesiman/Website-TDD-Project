from django.conf.urls import url
from .views import index, add_todo, delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_todo', add_todo, name='add_todo'),
    url(r'^delete/(?P<id>\d+)/$',delete, name ='delete'),
    #regex, keywordnya id yg isinya angka
]
