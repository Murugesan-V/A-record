"""ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from . import views
#from django.contrib.auth import views as login_view
from django.contrib.auth import views as login_view

from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.home , name='home_view'),
    url(r'create/' , views.create , name='create'),
    url(r'^delete/(?P<del_id>\d+)/$',views.delete,name='delete'),
    url(r'edit_record_details/(?P<edit_id>\d+)/' , views.edit_record_details , name='edit_record_details'),
    url(r'update/(?P<pk_id>\d+)',views.update_record,name='ajax'),
    url(r'ajax/',views.ajax,name='ajax'),
    
    url(r'accounts/',include('django.contrib.auth.urls')),
    url('login/',login_view.login,{'authentication_form':LoginForm}),
    #path('create', views.create_data, name='add_data')
]

'''
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as login_view
from .forms import LoginForm


urlpatterns = [
    url(r'^$',views.home,name='home_page'),
    url('login/',login_view.login,{'authentication_form':LoginForm}),
    url(r'signup/',views.signup,name='signup'),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r'data/',views.data,name='data' ),
    url(r'^delete/(?P<del_id>\d+)/$',views.delete,name='delete' )
]
'''
