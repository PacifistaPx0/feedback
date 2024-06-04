from django.db import models

# Create your models here.

#considered bad practice to store files in database, so we only store the path to the file
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
