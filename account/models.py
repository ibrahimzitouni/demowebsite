from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
class manager(BaseUserManager):
	def create_user(self,username,email,password):
		if not username or not email:
			raise ValueError("you must enter username or email")
		USERNAME = username
		EMAIL = self.normalize_email(email)
		user = self.model(email=EMAIL,username=USERNAME)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self,username,email,password):
		user = self.create_user(
			email = self.normalize_email(email) ,
			username = username , 
			password=password
			)
		user.is_admin         = True
		user.is_active        = True 
		user.is_staff         = True 
		user.is_superuser     = True
		user.save(using=self._db)
		return user
class Account(AbstractBaseUser):
	email            = models.EmailField(verbose_name='email',max_length=60,unique=True)
	username  		 = models.CharField(max_length=20,unique=True)
	date_joined      = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
	lasr_joined      = models.DateTimeField(verbose_name='last login',auto_now_add=True)
	is_admin         = models.BooleanField(default=False)
	is_active        = models.BooleanField(default=True)
	is_staff         = models.BooleanField(default=False)
	is_superuser     = models.BooleanField(default=False)
	password         = models.CharField(max_length=100)
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]
	objects = manager()
	def __str__(self):
		return self.username 
	def has_perm(self,perm,obj=None):
		return self.is_admin
	def has_module_perms(self,app_label):
		return True

class uploader(models.Model):
  title = models.CharField(max_length=40)
  file  = models.FileField()
  class Meta :
  	db_table = 'profile'


class blogform(models.Model):
  theID        = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  title        = models.CharField(max_length=30)
  body         = models.TextField(max_length=5000)
  publish_time = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
  update_time  = models.DateTimeField(auto_now=True, verbose_name='last login')
  image        = models.ImageField(upload_to='images')
  def __str__(self):
  	return self.title
"""
'ObjectDoesNotExist', 'utils', 'signals', 'constants' verbose_name verbose_name="" 
,auto_now_add,
, 'query_utils', 'fields', 'expressions', 'lookups', max_length ,
'functions', 'aggregates', 'Aggregate', 'Avg', 'Count'
, 'Max', 'Min', 'StdDev', 'Sum', 'Variance', 'aggregates_all'
, 'sql', 'constraints', 'CheckConstraint', 'UniqueConstraint',
 'constraints_all', 'deletion', 'CASCADE', 'DO_NOTHING', 'PROTECT'
 , 'SET', 'SET_DEFAULT', 'SET_NULL', 'ProtectedError', 'enums', 
 'Choices', 'IntegerChoices', 'TextChoices', 'enums_all', 'Case',
  'Exists', 'Expression', 'ExpressionList', 'ExpressionWrapper', 
  'F', 'Func', 'OuterRef', 'RowRange', 'Subquery', 'Value', 
  'ValueRange', 'When', 'Window', 'WindowFrame', 'AutoField', 
  'BLANK_CHOICE_DASH','BigAutoField', 'BigIntegerField', 'BinaryField'
  , 'BooleanField', 'CharField', 'CommaSeparatedIntegerField', 'DateField'
  , 'DateTimeField', 'DecimalField', 'DurationField', 'EmailField', 'Empty'
  , 'Field', 'FieldDoesNotExist', 'FilePathField', 'FloatField', 'GenericIPAddressField'
  , 'IPAddressField', 'IntegerField', 'NOT_PROVIDED', 'NullBooleanField',
   'PositiveIntegerField', 'PositiveSmallIntegerField', 'SlugField', 
   'SmallAutoField', 'SmallIntegerField', 'TextField', 'TimeField', 
   'URLField', 'UUIDField', 'fields_all', 'FileField', 'ImageField', 
   'OrderWrt', 'indexes', 'Index', 'indexes_all', 'Lookup', 'Transform'
   , 'query', 'manager', 'Manager', 'Prefetch', 'Q', 'QuerySet',
    'prefetch_related_objects', 'FilteredRelation', 'options', 'base', 
    'DEFERRED', 'Model', 'ForeignKey', 'ForeignObject', 'OneToOneField', 
    'ManyToManyField', 'ManyToOneRel', 'ManyToManyRel', 'OneToOneRel'
    """