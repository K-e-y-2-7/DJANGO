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


def main_article(request:HttpRequest) -> HttpResponse:   
    return HttpResponse('Main article')


def article(request:HttpRequest, article_number:int, name:str ='unnamed'):
    response = f'Article #{article_number}. Article name {name}.'
    return HttpResponse(response)


def archive_articles(request:HttpRequest, ) -> HttpResponse:   
    return HttpResponse('All articles in archive')


def archive_article(request:HttpRequest, article_number:int, name='' ) -> HttpResponse:   
    return HttpResponse('Article in archive')


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")
