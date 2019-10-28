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


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'ride_list'
    def get_queryset(self):
        return Ride.objects.all()
    
""" def AccountInfo(request):
    template = loader.get_template('accountInfo.html')

    context = {}

    return render(request, 'accountInfo.html', context=context) """
    
class RideView(CreateView):
    model = Ride
    template_name = 'create_ride.html'
    fields = ('origin', 'destination', 'departure_date', 'seats_available')
    def get_success_url(self):
            return ".."



