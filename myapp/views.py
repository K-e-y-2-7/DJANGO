from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def homepage(request: HttpRequest) -> HttpResponse:   
    return render(request, 'homepage.html')


def library(request: HttpRequest) -> HttpResponse:
    return render(request, 'library.html')


def users(request: HttpRequest) -> HttpResponse:
    return render(request, 'users.html')


def user(request:HttpRequest, user_number:int ) -> HttpResponse:   
    return render(request, 'user.html', {'number' : user_number})


def articles(request:HttpRequest) -> HttpResponse:    
    return render(request, 'articles.html')


def article(request:HttpRequest, article_number:int, name:str ='unnamed') -> HttpResponse:
    return render(request, 'article.html', {'number' : article_number, 'name' : name})


def archive_articles(request:HttpRequest, ) -> HttpResponse:   
    return render (request, 'archive_articles.html')


def archive_article(request:HttpRequest, article_number:int, ) -> HttpResponse:   
    return render (request, 'archive_article.html', {'number' : article_number})


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")
