from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .models import Ride

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

    #List all of the ride objects: NOT WORKING YET
    context_object_name = 'ride_list'
    def get_queryset(self):
        return Ride.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def AccountInfo(request):
    template = loader.get_template('accountInfo.html')

    context = {}

    return render(request, 'accountInfo.html', context=context)
    
class RideView(CreateView):
    model = Ride
    template_name = 'create_ride.html'
    fields = ('origin', 'destination', 'departure_date')
    def get_success_url(self):
            return ".."



