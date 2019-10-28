from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from .models import Ride
from django.db.models import F


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'ride_list'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None
        self.GET = None

    def get_queryset(self):
        return Ride.objects.all()

    def join_ride(self, request):
        if request.GET.get('joinRide'):
            ride = get_object_or_404(Ride, created_by=request.user)
            ride.seats_available = F('seats_available') - 1
            ride.save(update_fields=["seats_available"])
            return render(request, 'index.html')


def AccountInfo(request):
    template = loader.get_template('accountInfo.html')

    context = {}

    return render(request, 'accountInfo.html', context=context) """
    
class RideView(CreateView):
    model = Ride
    template_name = 'create_ride.html'
    fields = ('origin', 'origin_state', 'destination', 'destination_state', 'departure_date', 'seats_available')
    def get_success_url(self):
            return ".."



