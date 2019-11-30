"""ride_share_103_sharks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import logout,urls
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from rides import views

from django.conf.urls.static import static

# from django.contrib.auth.views import logout

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),  # index
    path('logout/', views.Logout),
    path('accounts/myaccount', views.Account_Info, name='accountInfo'),
    path('accounts/', include('django.contrib.auth.urls')),  # login
    path('create_ride/', views.RideView.as_view(), name='create_ride'), #Users can create a ride
    path('', include('social_django.urls', namespace='social')),
    url(r'(?P<ride_id>\d+)/(?P<join>\d+)/$', views.join_ride, name='join_ride'),
    url(r'(?P<ride_id>\d+)/$', views.delete_ride, name='delete_ride'),
    # url(r'^(?P<ride_id>\d+)/(?P<join>\d+)$', views.leave_ride, name='leave_ride'),
    path('', include('django.contrib.auth.urls')),

]
