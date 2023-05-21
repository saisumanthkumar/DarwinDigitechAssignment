from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class User(models.Model):
    username = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^[a-zA-Z]+$')])
    password = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z0-9@#$%^&+=]+$')])
    mobile = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
