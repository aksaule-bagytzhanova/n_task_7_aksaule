from django.shortcuts import render, redirect
from .models import Event, Booking

# Create your views here. 
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def register(request, pk):
    event = Event.objects.get(pk=pk)
    if request.user.is_authenticated:
        Booking.objects.create(user=request.user, event=event)
    return redirect('event_detail', pk=pk)