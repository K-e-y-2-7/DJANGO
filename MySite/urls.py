"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('articles/', include('myapp.urls')),
    path('comments/', views.comments, name='comments'), 
    path('last_five_comments/', views.five_comments, name='last_five_comments'),
    path('two_comments_of_article', views.two_comments_of_article, name='two_comments_of_article' ), 
    path('library/', views.library, name='library'), 
    path('users/', views.users, name='users'), 
    path('users/<int:user_number>', views.user, name='user'),
    re_path(r'^(?P<text>[\d,a-f]{4}-[\d,a-f]{6}$)', views.regex),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)