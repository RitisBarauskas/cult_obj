from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import CultureObject


class NewCultureObjectForm(ModelForm):
    class Meta:
        model = CultureObject
        fields = '__all__'


class SignUpForm(UserCreationForm):
    """
    Форма регистрации нового пользователя
    """

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
