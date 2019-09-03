from django import forms
from .models import RSVP

class RSVPFamily(forms.ModelForm):
	class Meta: 
		model = RSVP
		fields = ('First_Name', 'Family_Name', 'Email')