from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from api.managers import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    def validateEmail(email):
        if len(email) > 6:
            print(email,"11=-----------")
            if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) != None:
                return email
            else:
                raise ValidationError("Email entered is Incorrect.")
        raise ValidationError("Email is Incorrect")

    def validate_phone_number(value):
        if re.compile(r"\d{10}").match(value):
            return value
        else:
            raise ValidationError("Phone number entered is incorrect.")

    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(validators=[validateEmail],unique=True)
    phone_number = models.CharField(validators=[validate_phone_number], max_length=10, blank=True, null=True,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone_number"]
    objects = UserManager()

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    PRIORITY_CHOICES=(
        ("High","High"),
        ("Medium","Medium"),
        ("Low","Low"),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    task_name = models.CharField(max_length=100,blank=True,null=True)
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default='----')
    description = models.TextField(max_length=500,blank=True,null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.task_name}--{self.user.name}"

