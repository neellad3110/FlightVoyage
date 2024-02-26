from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,name,email,password, **extra_fields):
        """creating user"""
        if not email:
            raise ValueError("The Email is required.")
        user = self.model(email=self.normalize_email(email),name=name,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,name,email,password, **extra_fields):
        """creating super user"""
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(name,email,password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):

    id=models.CharField(default=uuid.uuid4,primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.email
