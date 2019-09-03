from django.shortcuts import render, redirect
from .models import RSVP
from django.http import HttpResponseRedirect
from .forms import RSVPFamily
from django.contrib import auth
import jobs.views

# Create your views here.
def InputRSVPFamily(request):
	if request.method == 'POST':
		form_RSVP=RSVPFamily(request.POST, request.FILES)
		if form_RSVP.is_valid():
			form_RSVP.save()
			return redirect(jobs.views.home)
	else:
		form_RSVP = RSVPFamily()
	return render(request, 'RSVP/rsvp_family.html', {'form' : form_RSVP})