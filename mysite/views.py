from mysite.models import contacts
from django.shortcuts import render , redirect
from django.http import HttpResponse as hr
from account.models import manager
from account.models import blogform
from os import system as do

def show(request):
	context = {}
	context['info'] = blogform.objects.all()
	return render(request,'mysite/base.html',context)