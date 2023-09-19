from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(requests):
	return render(requests,'homepage.html')


def index(requests):
	return render(requests,'index.html')