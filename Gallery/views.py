from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gallery(request):
    return render(request, 'Gallery/gallery.html')
    # return HttpResponse('Welcome to my Gallery')
