from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .usermanager import UserManager  # Assuming UserManager is in the same directory

class User(AbstractBaseUser,PermissionsMixin):
  """
  Custom user model using email as the unique identifier.
  """
  email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateTimeField(auto_now_add=True)
  is_staff = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()  # Assigning the custom user manager

  def __str__(self):
    return self.email
