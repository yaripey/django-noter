from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


from django.urls import reverse

from .forms import LoginForm, RegisterForm


@login_required
def index(request):
    notes = [{1, 'Note one'}, {2, 'Note two'}, {3, 'Note three'}, {4, 'Note four'}]

    return render(request, 'noter/index.html', {'notes': notes})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("kek")

    else:
        form = LoginForm()

    return render(request, 'noter/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("noter:index"))



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1']
            )
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.save()
            return redirect('noter:login')
    else:
        form = RegisterForm()

    return render(request, 'noter/register.html', {'form': form})
