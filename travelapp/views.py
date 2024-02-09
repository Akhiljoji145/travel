from django.shortcuts import render
from .models import Team,Places
# Create your views here.

def main(request):
	team=Team.objects.all()
	places=Places.objects.all()
	return render(request,'index.html',{'team':team,'places':places})

def news(request):
	return render(request,'news.html')

def contact(request):
	return render(request,'contact.html')