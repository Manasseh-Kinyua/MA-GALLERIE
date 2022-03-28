from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category,Location,Image

# Create your views here.
def gallery(request):
    images = Image.objects.all()
    # locations = Location.get_locations()
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
