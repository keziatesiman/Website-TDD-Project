from django.conf.urls import url
from .views import index, profile,add_session_drones, del_session_drones, clear_session_drones,cookie_login, cookie_auth_login, cookie_profile, cookie_clear, add_session_soundcards, del_session_soundcards, clear_session_soundcards, add_session_opticals, del_session_opticals, clear_session_opticals

# sol to challenge
#from .views import add_session_item, del_session_item, clear_session_item
# /sol
from .custom_auth import auth_login, auth_logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile/$', profile, name='profile'),

    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

    #add/delete drones
    url(r'^add_session_drones/(?P<id>\d+)/$', add_session_drones, name='add_session_drones'),
    url(r'^del_session_drones/(?P<id>\d+)/$', del_session_drones, name='del_session_drones'),
    url(r'^clear_session_drones/$', clear_session_drones, name='clear_session_drones'),

    #add/delete souncards
    url(r'^add_session_soundcards/(?P<id>\d+)/$', add_session_soundcards, name='add_session_soundcards'),
    url(r'^del_session_soundcards/(?P<id>\d+)/$', del_session_soundcards, name='del_session_soundcards'),
    url(r'^clear_session_soundcards/$', clear_session_soundcards, name='clear_session_soundcards'),

    #add/delete drones
    url(r'^add_session_opticals/(?P<id>\d+)/$', add_session_opticals, name='add_session_opticals'),
    url(r'^del_session_opticals/(?P<id>\d+)/$', del_session_opticals, name='del_session_opticals'),
    url(r'^clear_session_opticals/$', clear_session_opticals, name='clear_session_opticals'),

    # cookie
    url(r'^cookie/login/$', cookie_login, name='cookie_login'),
    url(r'^cookie/auth_login/$', cookie_auth_login, name='cookie_auth_login'),
    url(r'^cookie/profile/$', cookie_profile, name='cookie_profile'),
    url(r'^cookie/clear/$', cookie_clear, name='cookie_clear'), #sekaligus logout dari cookie

]
