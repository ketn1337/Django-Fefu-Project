from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .decorators import user_not_authenticated
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, ProductForm


@user_not_authenticated
def register(request):
    if request.user.is_authenticated:
        return redirect("profile/" + request.user.username)
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile/"+request.user.username)
    
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
                username = user.get_username()
                return redirect("profile/" + request.user.username)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = UserLoginForm()

    return render(
        request=request,
        template_name='users/login.html',
        context={'form': form}
    )


def profile(request, username):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
           
            return redirect("profile", user_form.username)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name="users/profile.html",
            context={"form": form}
            )
    
    return redirect("/")


def create_product(request, username):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save()
            product.save()
            previous_page = request.GET.get('next') if request.GET.get('next') is not None else ''
            return redirect(previous_page) if previous_page != '' else redirect('/')
    
    form = ProductForm()
    return render(request, 'users/create_product.html', {'form': form})


def buy_product(request, product_slug):
    product = get_object_or_404(request, product_slug)
    vk = product.vendor.vk
    product.delete()
    return redirect(f'{vk}')