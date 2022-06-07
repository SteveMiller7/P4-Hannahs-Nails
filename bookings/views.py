from django.shortcuts import render, redirect
from django.views import generic
from .models import Photo, MyBooking, Appointments
from .forms import AppointmentForm



def Index(request):
    # The View function for index/home page of site
    template_name = "index.html"
    context = {}
    return render(request, 'index.html', context=context)

class Inspiration(generic.ListView):
    # The View function for inspiration page page of site
    model = Photo
    template_name = 'inspiration.html'


def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer_name = request.user
            # The above line automatically adds the logged in users name to the back end booking when an appointment is made. 
            obj.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_bookings.html', {'form': form})


def BookingList(request):
    # The View function for inspiration page page of site
    booking_list = Appointments.objects.all()
    return render(request, 'my_appointments.html', {'booking_list': booking_list})

