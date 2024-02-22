from django.contrib import admin
from django.urls import path
from .views import *

'''urlpatterns = [
    path('admin/', admin.site.urls),
]
'''


class Login:
    pass


class Signup:
    pass


urlpatterns = [
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),

    path('',newhomepage, name='newhomepage'),
    path('card/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name ='print1'),
    path('print/',print_to_console,name='print-to-console'),
    path("ran1/",random123,name='random123'),
    path('ran/',ran,name='ran'),
    path('g/',getdate1,name='getdate1'),
    path('getdate/',get_date,name='get_date'),
    path('t/',timezfunc,name='timezfunc'),
    path('registerform/',registerform,name='registerform'),
    path('Register/',Register,name='Register'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('login1/',login1,name='login1'),
    path('contact/',contact,name='contact'),
    path('contactmail/',contactmail,name='contactmail'),



]
