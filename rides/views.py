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
from django.db.models import Q

#imports for profile:
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile
from .forms import UserForm,ProfileForm


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
        query = self.request.GET.get('search')
        select = self.request.GET.get('search_choice')
        if query == None:
            return Ride.objects.all()
        else :
            if(select == "origin"):
                object_list = Ride.objects.filter(
                    Q(origin__icontains=query) | Q(origin_state__icontains=query)
                )
                return object_list
            if(select == "destination"):
                object_list = Ride.objects.filter(
                    Q(destination__icontains=query) | Q(destination_state__icontains=query)
                )
                return object_list

    def join_ride(self, request):
        if request.GET.get('joinRide'):
            ride = get_object_or_404(Ride, created_by=request.user)
            ride.seats_available = F('seats_available') - 1
            ride.save(update_fields=["seats_available"])
            #user.ride_list.add(ride)
            return render(request, 'index.html')

@login_required
@transaction.atomic
def Account_Info(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accountInfo.html', { #was profile.html
        'user_form': user_form,
        'profile_form': profile_form
    })

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


class RideView(CreateView):
    model = Ride
    template_name = 'create_ride.html'
    fields = ('origin', 'origin_state', 'destination', 'destination_state', 'departure_date', 'asking_price', 'seats_available')
    def get_success_url(self):
            return ".."


def join_ride(request, **kwargs):
    id_to_join = kwargs['ride_id']
    is_join = kwargs['join']
    if is_join == '1':
        new_seats = Ride.objects.get(id=id_to_join).seats_available - 1
        if new_seats >= 0:
            Ride.objects.filter(id=id_to_join).update(seats_available=new_seats)
        Ride.objects.get(id=id_to_join).passenger_list.add(request.user)
        return render(request, 'join_ride.html')
    else:
        ride_to_leave = kwargs['ride_id']
        new_seats = Ride.objects.get(id=ride_to_leave).seats_available + 1
        Ride.objects.filter(id=ride_to_leave).update(seats_available=new_seats)
        Ride.objects.get(id=id_to_join).passenger_list.remove(request.user)
        return render(request, 'leave_ride.html')


# def leave_ride(request, **kwargs):
#
