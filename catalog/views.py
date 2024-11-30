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
    # Number of visits to this view
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

# BookListView
from django.views import generic
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4

# BookDetailView
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(generic.DetailView):
    model = Author
