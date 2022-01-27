from django.urls import path
from .views import main_article, article, archive_article

urlpatterns = [
    path('', main_article, name='mail_article'),
    path('<int:article_number>/', article, name='article'),
    path('<int:article_number>/archive', archive_article, name='article'),
    path('<int:article_number>/<slug:name>', article, name='article_name'),
]