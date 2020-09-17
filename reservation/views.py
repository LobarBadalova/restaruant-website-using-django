from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
# Create your views here.
def reservation(request):
	reserve_form=ReservationForm()
	if request.method=="POST":
		reserve_form=ReservationForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()

	context={'reserve_form':reserve_form}
	return render(request, 'Reservation/reservation.html', context)