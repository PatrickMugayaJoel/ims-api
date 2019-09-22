from datetime import datetime, timedelta

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


class BaseAccount(models.Model):
    """
    Base model class for creating company and user accounts
    """
    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=500)
    profile_pic = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True


class Company(BaseAccount):
    """
    Model class for creating Company accounts
    """
    company_name = models.CharField(db_index=True,
                                    max_length=255, unique=True)
    user_role = models.CharField(db_index=True, max_length=255,
                                 default='admin')

    REQUIRED_FIELDS = ['email', 'password', 'company_name']

    def __str__(self):
        # returns a string represantion of this company object
        return self.company_name

class User(BaseAccount):
    """
    Model class for creating User accounts
    """    
    first_name = models.CharField(db_index=True, max_length=255)
    last_name = models.CharField(db_index=True, max_length=255)
    user_role = models.CharField(db_index=True, max_length=255,
                                 default='normal_user')
    user_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

    def __str__(self):
        # Returns a string representation of this User object.
        
        return self.email
