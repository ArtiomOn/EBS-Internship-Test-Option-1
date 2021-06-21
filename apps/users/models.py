from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = EmailField(_('email address'), blank=False, unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
