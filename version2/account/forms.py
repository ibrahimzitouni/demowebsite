from django import forms 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from account.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(help_text='Required . add a valid email')
	class Meta :
		model = Account
		fields = ('email','username','password1','password2')

class AUTH(AuthenticationForm):
  username = forms.CharField()
  class Meta :
    model = Account
    fields = ('username','password')

class uploaderForm(forms.Form):
  title = forms.CharField(max_length=40)
  file  = forms.FileField()
    









"""
'ObjectDoesNotExist', 'utils', 'signals', 'constants'
, 'query_utils', 'fields', 'expressions', 'lookups', 
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