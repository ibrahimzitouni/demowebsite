from django.shortcuts import render , redirect
from django.http import HttpResponse as hr
from django.contrib.auth import login , authenticate , logout
from account.forms import RegistrationForm , AUTH , uploaderForm
from os import system
from account.models import uploader , blogform
def extention(x):
	x = [ y for y in x ]
	x.reverse()
	ls = []
	for i in x :
		if i == '.' :
			break
		else :
			ls.append(i)
	ls.reverse()
	x = ''
	for i in ls :
		x+=i
	return x
def listing(x):
	vide = ''
	ls=[]
	for y in x :
		if y == ';' :
			ls.append(vide)
			vide=''
		else :
			vide += y
	if vide != '' : ls.append(vide)
	return ls
def myitems(user):
	global ffile
	try:
		ffile = open(f'users/{user}/regiterta3lupload.txt','r')
	except FileNotFoundError :
		system(f'cd users & mkdir {user}')
		ffilee = open(f'users/{user}/regiterta3lupload.txt','w')
	READ = ffile.read()
	return listing(READ)
def show(request):
	context = {}
	info = blogform.objects.all()
	context['info'] = info
	return render(request,'main.html',context)
def uploading(request):
	system('cls')
	context= {}
	saved = False
	if request.POST :
		form = uploaderForm(request.POST,request.FILES)
		if form.is_valid():
			pfile = uploader()
			pfile.title = form.cleaned_data.get('title')
			pfile.title = pfile.title.replace(' ','_')
			pfile.file = form.cleaned_data.get('file')
			pfile.file.name = pfile.title + '.' + extention(pfile.file.name)
			try :
				ffilee = open(f'users/{request.user}/regiterta3lupload.txt','a')
			except FileNotFoundError :
				system(f'cd users & mkdir {request.user}')
				ffilee = open(f'users/{request.user}/regiterta3lupload.txt','w')
			ffilee.write(str(pfile.file)+';')
			ffilee.close()
			pfile.save()
			saved = True
			context['MYFORM'] = uploaderForm()
			context['succes'] = True
			return render(request,'mysite/upload.html',context)
		else :
			return render(request,'mysite/upload.html',context)
			print('not valid form')
	else :
		context['MYFORM'] = uploaderForm()
	return render(request,'mysite/upload.html',context)
def downloading(request):
	context = {
		"items" : myitems(user=str(request.user)) ,
	}
	return render(request,'mysite/download.html',context)