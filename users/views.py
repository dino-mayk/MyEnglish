from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from core.models import update_attrs
from users.forms import LoginForm, PasswordChange, SignUpForm, ProfileForm


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


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(
                data=request.POST,
                files=request.FILES,
                instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()

    form = ProfileForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'users/profile.html', context)


class PasswordChange(PasswordChangeView):
    form_class = PasswordChange
    success_url = reverse_lazy('password_change_done')
