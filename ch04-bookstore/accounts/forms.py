from django.contrib.auth import get_user_model  # noqa: D100
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):  # noqa: D101
    class Meta:  # noqa: D106
        model = CustomUser
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):  # noqa: D101
    class Meta:  # noqa: D106
        model = CustomUser
        fields = (
            "email",
            "username",
        )
