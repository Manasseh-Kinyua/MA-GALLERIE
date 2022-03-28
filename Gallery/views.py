from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category,Location,Image

# Create your views here.
def gallery(request):
    location = request.GET.get("location")

    if location == None:
        locations = Location.objects.all()
    else:
        locations = Location.objects.filter(location__icontains=location)

    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'Gallery/gallery.html', {"images": images, "locations":locations})

def photo(request, pk):
    image = Image.objects.get(id = pk) 
    return render(request, 'Gallery/photo.html', {"image":image})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_image(category)
        message = f"{category}"
        return render(request, 'Gallery/search.html', {"message":message, "images":searched_images})
    else:
        message = "You have not searched any images"
        return render(request, 'Gallery/search.html', {"message":message})
