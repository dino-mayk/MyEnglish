from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserChangeForm, UserCreationForm)

from users.models import CustomUser


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'avatar')
        labels = {
            CustomUser.username.field.name: 'Имя пользователя',
            CustomUser.avatar.field.name: 'аватарка'
        }


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'avatar',
        )
        labels = {
            'first_name': 'Имя',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class PasswordChange(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
