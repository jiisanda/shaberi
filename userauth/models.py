from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio, number, picture
    bio = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True, default='profile_pics/default_profile.png')
    
    def __str__(self):
        return str(self.user.username)
    
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_picture.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path)
