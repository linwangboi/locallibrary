from django.shortcuts import render

# Create your views here.

# Sadie added
from .models import Book, Author, BookInstance, Genre

def index(request):
    '''View function for home page of site.'''
    # generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # the all() is implied by default.
    num_authors = Author.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }
    return render(request, 'index.html', context=context)

# BookListView
from django.views import generic
class BookListView(generic.ListView):
    model = Book

# BookDetailView
class BookDetailView(generic.DetailView):
    model = Book