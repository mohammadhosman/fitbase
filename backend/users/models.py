from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .managers import CustomUserManager

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    #password
    first_name = models.CharField(max_length=50)

    #Additional profile and personal info
    #Might creae a separate UserProfile model and create a one-to-one relationship
    #between User and UserProfile
    last_name = models.CharField(max_length=50, 
                                blank=True, null=True)
    #Using regex to validate phone numbers entered when a user creates an account
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #Might use "django-phonenumber-field" package instead. Still a maybe though becuase it's a big package
    #Source: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    bio = models.TextField(max_length=1200 ,blank=True, null=True)

    def __str__(self):
        return self.username