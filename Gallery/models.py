from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.image_name

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.location

class Location(models.Model):
    location = models.CharField(max_length = 100)



