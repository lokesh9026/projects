from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView,UpdateView
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

#################### home #######################################
def HomeView(request):
    return render ( request ,"home.html")

########### register here #####################################
def SignupView(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			if User.objects.filter(email=email):
				raise ValidationError("EMAIL ALREADY EXISTS")
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'signup.html', {'form': form, 'title':'reqister here'})

################ login forms###################################################
def LoginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			item = Book.objects.all()
			print(item)
			# return redirect('dashboard')
			return render(request, 'dashboard.html', {'book':item})
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'login.html', {'form':form, 'title':'log in'})

@login_required(login_url='login')
def Dashboard(request):
	item=Book.objects.all()
	return render ( request ,"dashboard.html",{'book':item})


# @method_decorator(login_required, name='addbook')
class AddbookView(LoginRequiredMixin,CreateView):
    model = Book
    template_name = 'addbook.html'
    success_url = '/dashboard/'
    fields = ['name', 'Author','price']


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'deletebook.html'
    success_url = "/dashboard/"


class UpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['name', 'Author','price']
    template_name = 'updatebook.html'
    success_url = '/dashboard/'


def LogoutView(request):
    logout(request)
    return redirect("home")