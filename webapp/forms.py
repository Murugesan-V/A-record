from django import forms 
from . import models 

# class BookForm(forms.ModelForm):
# 	class Meta:
# 		model= models.Book
# 		fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )

from django import forms


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm) :
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
