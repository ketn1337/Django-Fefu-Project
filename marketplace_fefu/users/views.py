from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .decorators import user_not_authenticated
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm


@user_not_authenticated
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('/')
    
    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name='users/registration.html',
        context={'form': form})


@login_required
def cust_logout(request):
    logout(request)
    return redirect('/')


@user_not_authenticated
def cust_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = UserLoginForm()

    return render(
        request=request,
        template_name='users/login.html',
        context={'form': form}
    )

def profile(request,  username):
    if request.method == 'POST':
        user = request.user
        form =  form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            return redirect("profile", user_form.username)
        
        for error in list(form.errors.values()):
            messages.error(request, error)

        
        user = get_user_model().objects.filter(username=username).first()

        if user:
            form = UserUpdateForm(instance=user)

            form.fields['description'].widget.attrs = {'rows': 1}
            return render(
                request=request,
                template_name="users/profile.html",
                context={"form": form}
                )
    
    return redirect("/")
        
