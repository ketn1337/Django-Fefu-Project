from django.forms import ModelForm, models, Form
from products.models import Product
from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']
    
    def save(self, commit=True):
        product = super(ProductForm, self).save(commit=False)
        if self.cleaned_data['image']:
            product.image = self.cleaned_data['image']
            product.save()
        return product


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username','vk', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
    
class UserLoginForm( AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'vk']

