from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username= forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}

    def __str__(self):
        return f"username:{self.username} - email:{self.email} - password1:{self.password1}"

class UserEditForm(UserChangeForm):
    username= forms.CharField(label="ingrese su usuario")
    password= None
    email= forms.EmailField(label="ingrese su email")
    imagen= forms.ImageField(label="Avatar", required= False)


    class Meta:
        model= User
        fields= {"email", "password", "username"}