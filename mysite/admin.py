from django.contrib import admin
from mysite.models import contacts
try:
	from django.contrib.admin import site
	site.register(contacts)
except :
	raise ValueError(site.__dir__())