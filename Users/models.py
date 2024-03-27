from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add your custom fields here

    class Meta:
        # Add any additional options for your model's meta
        pass

class MyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_model_user')
    # Add your other fields here
