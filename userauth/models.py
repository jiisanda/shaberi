from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,default=None, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # bio, number, picture
    bio = models.TextField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, default='default_profile.jpg')
    
    def __str__(self):
        return str(self.user.username)
