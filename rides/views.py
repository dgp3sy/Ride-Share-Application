from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def IndexView(request):
    template = loader.get_template('index.html')



    """View function for home page of site."""

    # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    #
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #
    # # The 'all()' is implied by default.
    # num_authors = Author.objects.count()

    # context = {
    #     'num_books': num_books,
    #     'num_instances': num_instances,
    #     'num_instances_available': num_instances_available,
    #     'num_authors': num_authors,
    # }
    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def AccountInfo(request):
    template = loader.get_template('accountInfo.html')

    context = {}

    return render(request, 'accountInfo.html', context=context)