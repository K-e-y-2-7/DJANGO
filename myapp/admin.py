from logging import Filter
from django.contrib import admin
import myapp.models

#==============================================================================
#                                   LIBRARY
#==============================================================================

@admin.register(myapp.models.BookAuthor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(myapp.models.BookReaders)
class BookReadersAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(myapp.models.Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_of_published', 'are_available']
    list_filter = ['name', 'year_of_published']


#==============================================================================
#                                   BLOG-SITE
#==============================================================================

@admin.register(myapp.models.ArticleAuthor)
class ArticleAuthorAdmin(admin.ModelAdmin):
    list_display = ['pseudonym']
    list_filter = ['name', 'pseudonym']

@admin.register(myapp.models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'headline', 'text', 'genre', 'created_at', 'updated_at']
    list_filter = ['author', 'headline', 'genre', 'created_at',]
@admin.register(myapp.models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'comment', 'article', 'created_at', 'updated_at']
    list_filter = ['user', 'comment', 'article', 'created_at',]
@admin.register(myapp.models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['article', 'comment', 'user']
    list_filter = ['user', 'comment', 'article',]
@admin.register(myapp.models.Dislike)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ['article', 'comment', 'user']
    list_filter = ['user', 'comment', 'article',]