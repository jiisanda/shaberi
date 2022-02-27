from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio, number, picture
    bio = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default_profile.jpg')
    
    def __str__(self):
        return str(self.user.username)
