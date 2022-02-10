from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('archive',views.archive_articles),
    path('<int:article_number>/', views.article, name='article'),
    path('<int:article_number>/archive', views.archive_article, name='article'),
    path('<int:article_number>/<slug:name>', views.article, name='article_name'),
]