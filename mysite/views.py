import django.http
import django.http.request
from django.http import  HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from .forms import UserRegisterForm
from .functions import handle_uploaded_file
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


#################### index#######################################
def index(request):
	 return render(request, 'index.html', {'title':'index'})
	# return  redirect('register')
########### register here #####################################
def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request, username+f' has been created ! You are now able to log in')
			return redirect('index')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form, 'title':'reqister here'})

################ login forms###################################################
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exist ')
	form = AuthenticationForm()
	return render(request, 'login.html', {'form':form, 'title':'log in'})

def logoutUSer(request):
	logout(request)
	return redirect('login')
def index(request):
    return render(request,'index.html')

################ UPLOAD ###################################################
# @login_required(login_url='login')
# def upload(request):
# 	if request.method == 'POST' and request.FILES['upload']:
# 		upload = request.FILES['upload']
# 		fss = FileSystemStorage()
# 		file = fss.save(upload.name, upload)
# 		file_url = fss.url(file)
# 		return render(request, 'upload.html', {'file_url': file_url})
# 	return render(request, 'upload.html')


# def upload(request):
# 	if request.method == "POST":
# 		form = MovieForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("main:upload")
# 	form = MovieForm()
# 	movies = Movie.objects.all()
# 	return render(request=request, template_name="main/upload.html", context={'form':form, 'movies':movies})



