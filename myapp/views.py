from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def homepage(request: HttpRequest) -> HttpResponse:   
    return HttpResponse('HOME')


def users(request: HttpRequest) -> HttpResponse:   
    return HttpResponse('All people')


def user(request:HttpRequest, user_number:int ) -> HttpResponse:   
    return HttpResponse(f'User #{user_number}')


def articles(request:HttpRequest) -> HttpResponse:   
    return HttpResponse('All articles')


def main_article(request:HttpRequest) -> HttpResponse:   
    return HttpResponse('Main article')


def article(request, article_number:int, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_number, "Name of this article is {}".format(
            name) if name else "This is unnamed article")) 


def archive_articles(request:HttpRequest, ) -> HttpResponse:   
    return HttpResponse('All articles in archive')


def archive_article(request:HttpRequest, article_number:int, name='' ) -> HttpResponse:   
    return HttpResponse('Article in archive')


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")
