# import jwt

from datetime import datetime, timedelta

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):

    def create_account(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user
    def create_company(self, email, company_name, password=None):
        self.create_account(email)


class Company(models.Model):

    company_name = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(db_index=True, unique=True)

    password = models.CharField(max_length=500)

    is_active = models.BooleanField(default=True)

    user_role = models.CharField(db_index=True, max_length=255, default='admin')

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)

    deleted_at = models.DateField(null=True)

    REQUIRED_FIELDS = ['email', 'password', 'company_name']


    def __str__(self):
        return self.company_name

class User(models.Model):
    
    first_name = models.CharField(db_index=True, max_length=255)

    last_name = models.CharField(db_index=True, max_length=255)

    email = models.EmailField(db_index=True, unique=True)

    password = models.CharField(max_length=500)

    is_active = models.BooleanField(default=True)

    user_role = models.CharField(db_index=True, max_length=255, default='normal_user')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    user_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    is_staff = models.BooleanField(default=False)

    deleted = models.BooleanField(default=False)

    deleted_at = models.DateField(null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        """
        return self.email
