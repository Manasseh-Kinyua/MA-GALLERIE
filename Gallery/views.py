from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Location,Image

# Create your views here.
def gallery(request):
    images = Image.objects.all()
    return render(request, 'Gallery/gallery.html', {"images": images})
