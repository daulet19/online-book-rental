from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def zhanry(request):
    return render(request, 'mainApp/zhanry.html')

def onas(request):
    return render(request, 'mainApp/onas.html')

def avtory(request):
    return render(request, 'mainApp/avtory.html')



from mainApp.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'mainApp/homePage.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
