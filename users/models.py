from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    """
    Custom user manager where email is the unique identifier
    for authentication instead of username.
    """

    def create_user(self, phone, last_name, first_name, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.
        """
        if not phone:
            raise ValueError(_('The phone field must be set'))
        if not last_name:
            raise ValueError(_('Enter last_name'))
        if not first_name:
            raise ValueError(_('Enter first_name'))

        user = self.model(phone=phone, last_name=last_name, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, last_name, first_name, password=None, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(phone, last_name, first_name, password, **extra_fields)


class User(AbstractUser):
    email = None
    username = None
    phone = models.CharField(unique=True, max_length=20, verbose_name="Телефон")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['last_name', 'first_name']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
