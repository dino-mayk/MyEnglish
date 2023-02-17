from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from core.models import update_attrs
from users.forms import (
    SignUpForm,
    LoginForm,
    PasswordChange
)


def signup(request):
    form = SignUpForm(data=request.POST, files=request.FILES)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_attrs(user, is_shelter=False)
        messages.success(request, 'Вы успешно зарегистрировались')
        login(request, user)
        return redirect('homepage:home')
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


class Login(LoginView):
    form_class = LoginForm


def profile(request):
    return 'hello'


class PasswordChange(PasswordChangeView):
    form_class = PasswordChange
    success_url = reverse_lazy('password_change_done')
