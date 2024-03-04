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


class User(AbstractBaseUser,PermissionsMixin):

    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
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
