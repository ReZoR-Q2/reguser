from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Импортируйте вашу модель

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Используйте вашу модель
        fields = ("username", "email", "password1", "password2")