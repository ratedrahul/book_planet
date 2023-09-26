from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView
import os
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm,BookUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *

# Create your views here.
def view_pdf(request, pdf_filename):
	try:
		pdf_filename = 'book_collection/'+pdf_filename
		file_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)

		with open(file_path, 'rb') as pdf_content:
		    response = HttpResponse(pdf_content.read(), content_type='application/pdf')
		    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
		    return response
	except:
		return HttpResponse("PDF file not found", status=404)


def upload_to(request):
	if request.method =='POST':
		form = BookUploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Book uploaded successfully')
			return redirect(('homepage'))
		else:
			print('form validation error in file upload',form.errors)
	form = BookUploadForm()
	return render(request,'upload.html',{'form':form})



def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			user = form.save()
			return redirect('login')
		pass
	else:
		form = RegistrationForm()
	return render(request,'register.html',{'form':form})


def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		print(request.POST)
		if form.is_valid():
			print(request.POST)
			username = form.cleaned_data.get('username')
			password = forms.cleaned_data.get('password')
			user = authenticate(username= username,password= password)
			if user is not None:
				messages.success(request, f"logged in as {username}")
				return HttpResponseRedirect('homepage')
			else:
				print('errorororooror')
		else:
			print('-------',form.errors)
			messages.error(request, "form.errors")

	else:
		form = LoginForm()
	return render(request,'login.html',{'form':form})



def homepage(request):
	return render(request,'homepage.html')

def index(request):
	return render(request,'index.html')


def blog(request):
	return render(request,'blog.html')


def coding_books(request):
	data = Book.objects.filter(category__category__contains='coding')
	data_liss = []

	for file in data:
		context_data = {}
		context_data['url'] = str(file.storage_path.book_storage)
		context_data['title'] = file.title
		data_liss.append(context_data)
	return render(request,'coding_books.html',{'data':data_liss})


# def register(request):
# 	form = UserCreationForm()  
# 	context = {'form':form}
# 	return render(request, 'register.html', context)  



# class CustomLoginView(LoginView):
#     template_name = 'login.html'



# class RegistrationView(CreateView):
# 	form = UserCreationForm()
# 	template_name = 'register.html'


# def login(request):
# 	form = UserCreationForm()  
# 	context = {'form':form}
# 	return render(request, 'login.html', context)  


