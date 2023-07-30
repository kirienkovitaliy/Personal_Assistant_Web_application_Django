from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, EmailField, EmailInput, PasswordInput


class RegisterForm(UserCreationForm):
    """
    Form for user registration.

    Attributes:
        username (CharField): Field for the username.
        first_name (CharField): Field for the user's first name.
        last_name (CharField): Field for the user's last name.
        email (EmailField): Field for the user's email.
        password1 (CharField): Field for the user's password.
        password2 (CharField): Field to confirm the user's password.
    """

    username: CharField = CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
    )
    first_name: CharField = CharField(
        max_length=150,
        required=False,
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Firstname"}),
    )
    last_name: CharField = CharField(
        max_length=150,
        required=False,
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Lastname"}),
    )
    email: EmailField = EmailField(
        max_length=150,
        required=True,
        widget=EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    password1: CharField = CharField(
        max_length=12,
        min_length=8,
        required=True,
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    password2: CharField = CharField(
        max_length=12,
        min_length=8,
        required=True,
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class LoginForm(AuthenticationForm):
    """
    Form for user login.

    Attributes:
        username (CharField): Field for the username.
        password (CharField): Field for the user's password.
    """

    username: CharField = CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
    )
    password: CharField = CharField(
        max_length=12,
        min_length=8,
        required=True,
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password")
