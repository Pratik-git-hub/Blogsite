from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post1
from captcha.fields import CaptchaField
from captcha.helpers import math_challenge



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    captcha = CaptchaField()




    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class PostForm(forms.ModelForm,forms.Form):
    print("how atre you")

    class Meta():
        model = Post1
        fields = ('title','text','image1','is_public')

        widgets = {
            'title' : forms.TextInput(attrs={'class':
                                             'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable '
                                                  'medium-editor-textarea postcontent'}),

        }