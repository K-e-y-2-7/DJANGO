from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('archive',views.archive_articles, name='archive'),
    path('<int:article_number>/', views.article, name='article'),
    path('<int:article_number>/comments', views.article_with_comments, name='article-with-comments'),
    path('<int:article_number>/archive', views.archive_article, name='article-in-archive'),
    path('<int:article_number>/<slug:name>', views.article, name='article-name'),
]