from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,default=None, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # bio, number, picture
    bio = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, default='default_profile.jpg')
    
    def __str__(self):
        return str(self.user.username)
