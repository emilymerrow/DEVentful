from django.shortcuts import render, redirect
from .models import Vendor, Event

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Corrected function call
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'error_message': error_message, 'form': form})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'event_type', 'event_date', 'start_time',
               'end_time', 'location', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventList(LoginRequiredMixin, ListView):
    model = Event

@login_required
def event_index(request):
    events = Event.objects.filter(user=request.user)  # Corrected queryset
    return render(request, 'events/index.html', {'events': events})


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['event_name', 'event_date', 'start_time', 
              'end_time', 'location', 'description']
    success_url = '/events/'

class VendorCreate(CreateView):
    model = Vendor
    fields = ['vendor_name', 'description', 'category', 
              'cost', 'poc', 'email', 'phone']
    
class VendorList(ListView):
    model = Vendor

class VendorDetail(DetailView):
    model = Vendor

class VendorDelete(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = '/vendors/'

class VendorUpdate(LoginRequiredMixin, UpdateView):
    model = Vendor
    fields = ['vendor_name', 'description', 
              'cost', 'poc', 'email', 'phone']