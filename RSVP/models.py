from django.db import models

class RSVP(models.Model):
	First_Name = models.CharField(max_length=50, blank=False)
	Family_Name = models.CharField(max_length=50, blank=True)
	Email = models.EmailField()
	