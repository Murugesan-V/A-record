
from django import forms

from .models import arecord_users,validation

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm) :
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	

class PostForm(forms.ModelForm):

    class Meta:
        model = validation
        fields = ('domain_name','public_key','private_key')

class PostForm1(forms.ModelForm):
   domain_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   redirect_to_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   permanent = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   parameter_copy = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   request_path = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   domain_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   updated_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   ssl_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   class Meta:
        model = arecord_users
        fields = ('domain_name','redirect_to_url','region','permanent','parameter_copy','request_path','domain_type','status','updated_date','ssl_status')



