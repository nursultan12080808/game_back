from django import forms
from game_app.models import Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

class GamesForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = (
            'name',
            'price',
            'content',
            'image',
            'category',
            'tag',
        )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'user_permissions',
            'groups',
            'last_login',
            'password'
        )


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ChangePasswordForm(forms.Form):

    def __init__(self, user=None, *args, **kwargs):
        self.user: User = user
        super().__init__(*args, **kwargs)

    password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    game_password = forms.CharField(label='Новый пароль', validators=[validate_password],)
    confirm_password = forms.CharField(label='Подтвердите пароль')

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')

        if not self.user.check_password(password):
            raise forms.ValidationError({'password': ['Пароль не коректный']})

        game_password = cleaned_data.get('game_password')
        confirm_password = cleaned_data.get('confirm_password')

        if confirm_password != game_password:
            raise forms.ValidationError({'confirm_password': ['Пароли не совпадают']})

        return cleaned_data