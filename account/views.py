from django.shortcuts import render , redirect
from django.http import HttpResponse as hr
from django.contrib.auth import login , authenticate , logout
from account.forms import RegistrationForm , AUTH 
from os import system
def Registraion(request):
	context = {}
	if request.POST :
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password1')
			accounting = authenticate(email=email,password=password1)
			authentication = authenticate(username=username,password=password1)
			login(request,authentication)
			return render(request,'mysite/base.html',context)
		else :
			context['MYFORM'] = form
			return render(request,'mysite/reg.html',context)
	else  :
		form = RegistrationForm()
		context['MYFORM'] = form
	return render(request,'mysite/reg.html',context)

def _logInOUT(_request):
	logout(_request)
	return redirect('show')

def _login(request):
	system('cls')
	context = {}
	if request.POST :
		username = request.POST['username']
		password = request.POST['password']
		authentication = authenticate(username=username,password=password)
		if authentication :
			login(request,authentication)
			return redirect('show')
		else :
			form = AUTH(request.POST)
			context['MYFORM'] = form
			context['notlogin'] = "Username or Password Incorrect !"
			return render(request,'mysite/login.html',context)
	else  :
		form = AUTH()
		context['MYFORM'] = form
		return render(request,'mysite/login.html',context)
