"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from authentication.views import login_view
from authentication.views import logout_view
from authentication.views import signup_view
from notification.views import notifications_view
from tweet.views import create_tweet_view
from tweet.views import tweet_detail_view
from twitteruser.views import follow_user_view
from twitteruser.views import index_view
from twitteruser.views import user_detail_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('', index_view, name='homepage'),
    path('user/<str:username>/', user_detail_view, name='user_detail'),
    path('user/<str:username>/follow/', follow_user_view, name='follow_user'),
    path('tweet/<int:tweet_id>/', tweet_detail_view, name='tweet_detail'),
    path('tweet/new/', create_tweet_view, name='create_tweet'),
    path('notifications/', notifications_view, name='notifications'),
    path('admin/', admin.site.urls),
]
