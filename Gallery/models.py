from unicodedata import name
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length = 50)

    def save_location(self):
        self.save()

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.location

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    image_name = models.CharField(max_length = 50)
    image_description = models.TextField()
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(image_category__name__icontains=category)
        return images

    class Meta:
        ordering = ['image_name']