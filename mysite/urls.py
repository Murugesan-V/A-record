"""including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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

