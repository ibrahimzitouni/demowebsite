from django.contrib import admin
from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin
from account.models import Account , blogform
class helperadmi(UserAdmin):
	filter_horizontal = []
	list_filter = ()
	list_display = ('username','email','is_admin')
	search_fields = ('username','email')
site.register(Account)#,helperadmi)
site.register(blogform)