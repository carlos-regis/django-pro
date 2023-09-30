from django.contrib.auth import get_user_model  # noqa: D100
from django.test import TestCase

User = get_user_model()


class CustomUserTests(TestCase):  # noqa: D101
    def test_create_user(self):  # noqa: ANN101, ANN201, D102
        user = User.objects.create_user(
            username="will", email="will@email.com", password="testpass123"  # noqa: COM812, E501, Q000, S106
        )
        assert user.username == "will"  # noqa: Q000, S101
        assert user.email == "will@email.com"  # noqa: Q000, S101
        assert user.is_active  # noqa: S101
        assert not user.is_staff  # noqa: S101
        assert not user.is_superuser  # noqa: S101

    def test_create_superuser(self):  # noqa: ANN101, ANN201, D102
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"  # noqa: COM812, E501, Q000, S106
        )
        assert admin_user.username == "superadmin"  # noqa: Q000, S101
        assert admin_user.email == "superadmin@email.com"  # noqa: Q000, S101
        assert admin_user.is_active  # noqa: S101
        assert admin_user.is_staff  # noqa: S101
        assert admin_user.is_superuser  # noqa: S101
