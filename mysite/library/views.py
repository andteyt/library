from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
    author = Authors.objects.all()  #select_related(id)
    book = Books.objects.all()
    context = {'author': author, 'books': book}
    return render(request, 'library/index.html', context)

def Genres(request):
    Genres = Genres.objects.select_related(id)
    context = {'Genres': Genres}
    return render(request, 'library/Genres.html', context)

def author(request,author_id):
    author = Authors.objects.get(pk=author_id)
    books = Books.objects.filter(authors=author_id)
    context = {'Author': author, 'books': books}
    return render(request, 'library/author.html', context)

def book(request,book_id):
    book = Books.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'library/book.html', context)


