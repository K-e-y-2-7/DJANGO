import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

#==============================================================================
#                                   LIBRARY
#==============================================================================

class BookAuthor (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
        ordering = ['name', 'surname']
        verbose_name_plural = 'BookAuthors'

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class BookReaders (models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
            ordering = ['name', 'surname']
            verbose_name_plural = 'BookReaders'
    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Books (models.Model):
    author = models.ManyToManyField(BookAuthor)
    are_available = models.BooleanField(default=True)
    img = models.ImageField(upload_to='media/images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    year_of_published = models.DateField()
    readers = models.ManyToManyField(BookReaders, blank=True)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Books'

    def __str__(self) -> str:  
        return f'''Name of the book: {self.name}; Date of published:
{self.year_of_published}; Author of the book: {[str(author) for author in self.author.all()]}'''


#==============================================================================
#                                   BLOG-SITE
#==============================================================================

GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)


class ArticleAuthor(models.Model):
    pseudonym = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.pseudonym


class Article(models.Model):
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, null=True, related_name='articles')
    created_at = models.DateTimeField(default=timezone.now)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)
    headline = models.CharField(max_length=100)
    text = models.TextField(null=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['headline']
        

    def __str__(self):
        return f"Headline - {self.headline} Author - {self.author}, genre - {self.genre}, id - {self.id}"


class Comment(models.Model):
    article= models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=True, null=True)
    comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
       
    def __str__(self): 
        return f'''🗣 {self.text}
                                                        by {self.user}'''
                                                        
    def save(self, **kwargs):
        if not self.id:
            self.created_at = timezone.now() - datetime.timedelta(days=365) + datetime.timedelta(hours=2)
        super().save(**kwargs)


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"👍 By user {self.user} to {self.article or self.comment}"


class Dislike(models.Model):   
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"👎 By user {self.user} to {self.article or self.comment}"