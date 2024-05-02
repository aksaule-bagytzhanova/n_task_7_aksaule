from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
    return render(request, 'my_bookings.html', {'bookings': bookings})