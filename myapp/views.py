from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

import myapp.models


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'homepage.html')


def library(request: HttpRequest) -> HttpResponse:
    books = myapp.models.Books.objects.all()
    return render(request, 'library.html', {'books': books})


def users(request: HttpRequest) -> HttpResponse:
    return render(request, 'users.html')


def user(request:HttpRequest, user_number:int) -> HttpResponse:
    return render(request, 'user.html', {'number' : user_number})


def articles(request:HttpRequest) -> HttpResponse:
    articles = myapp.models.Article.objects.all()
    likes = myapp.models.Like.objects.all()
    dislikes = myapp.models.Dislike.objects.all()
    return render(request, 'articles.html', {
        'articles' : articles,
        'likes' : likes,
        'dislikes' : dislikes
         })


def article(request:HttpRequest, article_number:int, name:str ='unnamed') -> HttpResponse:
    article = myapp.models.Article.objects.get(id=article_number)
    likes = myapp.models.Like.objects.all()
    dislikes = myapp.models.Dislike.objects.all()
    return render(request, 'article.html', {
        'number' : article_number,
        'name' : name,
        'article' : article,
        'likes' : likes,
        'dislikes' : dislikes
        })


def article_with_comments(request:HttpRequest, article_number:int, name:str ='unnamed') -> HttpResponse:
    article = myapp.models.Article.objects.get(id=article_number)
    likes = myapp.models.Like.objects.all()
    dislikes = myapp.models.Dislike.objects.all()
    comments = myapp.models.Comment.objects.all() 
    return render(request, 'article_with_comments.html', {
        'number' : article_number,
        'name' : name,
        'article' : article,
        'likes' : likes,
        'dislikes' : dislikes,
        'comments' : comments,
        })


def archive_articles(request:HttpRequest) -> HttpResponse:
    return render (request, 'archive_articles.html')


def archive_article(request:HttpRequest, article_number:int) -> HttpResponse:
    return render (request, 'archive_article.html', {'number' : article_number})


def comments(request:HttpRequest) -> HttpResponse:
    return render (request, 'comments.html')


def two_comments_of_article(request):
    author = myapp.models.ArticleAuthor.objects.order_by('-pseudonym')[:1]
    for elem in author:
        author = elem.pseudonym
    articles = myapp.models.Article.objects.filter(author__pseudonym__icontains=author)

    comments = myapp.models.Comment.objects.filter(article__author__pseudonym__icontains=author).order_by('created_at')[:2]
    likes = myapp.models.Like.objects.all()
    dislikes = myapp.models.Dislike.objects.all()
    return render (request, 'two_comments.html',{
        'comments': comments,
        'articles' : articles,
        'likes' : likes,
        'dislikes' : dislikes
    })


def five_comments(request:HttpRequest) -> HttpResponse:
    comment1 = myapp.models.Comment.objects.create(text='Start of this comment. Some text ...', user=User.objects.get(id=1)) 
    comment2 = myapp.models.Comment.objects.create(text='A large comment ...', user=User.objects.get(id=1))
    comment3 = myapp.models.Comment.objects.create(text='Some text... here is Middle of the comment. Some text..', user=User.objects.get(id=1))
    comment4 = myapp.models.Comment.objects.create(text='Some random text...', user=User.objects.get(id=1))
    comment5 = myapp.models.Comment.objects.create(text='...', user=User.objects.get(id=1))
    comments = [comment1, comment2, comment3, comment4, comment5,]
    likes = myapp.models.Like.objects.all()
    dislikes = myapp.models.Dislike.objects.all()

    #4) Изменить комментарии со словами "Start", "Middle", "Finish".
    #Comment.objects.filter(text__istartswith = 'Start').update(text = 'bla-bla')
    #Comment.objects.filter(text__icontains='Middle').update(text = 'la-la-la')
    #Comment.objects.filter(text__iendswith = 'Finish.').update(text = 'ta-ta-ta')

    #5) Удалить все комментарии у которых в тексте есть буква "k", но не удалять если есть буква "с". 
    #Comment.objects.filter(text__icontains='k').exclude(text__icontains='c').delete()

    #Comment.objects.filter(сomment__user__id ='1').exclude(text__icontains='some').filter(created_at__gte__=datetime.today)
    return render (request, 'last_five_comments.html',{
    'comments' : comments,
    'likes' : likes,
    'dislikes' : dislikes
    })


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")
