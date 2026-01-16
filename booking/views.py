from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import CourtBooking
from .forms import CourtBookingForm
from django.contrib.auth.decorators import login_required

@login_required
def booking_list(request):
   print("Logged in user:", request.user)
   bookings = CourtBooking.objects.filter(user=request.user)
   return render(request, 'booking/booking_list.html', {'bookings': bookings})
   

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = CourtBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = CourtBookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(CourtBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CourtBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = CourtBookingForm(instance=booking)
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(CourtBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})
