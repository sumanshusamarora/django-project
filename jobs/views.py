from django.shortcuts import render
from .models import Job

def home(request):
	jobobjects = Job.objects
	return render(request, 'jobs/home.html', {'jobobjects':jobobjects})

def uploadpicture(request):
	return render(request, 'jobs/picture-upload-form.html')