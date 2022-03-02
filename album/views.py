from django.shortcuts import render,redirect
from django.http import HttpResponse

from album.models import Image,Category,Location

# Create your views here.
def index(request):
  images = Image.objects.all()
  return render(request,'index.html',{"images":images,})

def location(request,location):
  images = Image.filter_by_location(location)
  location = Location.objects.all()

  return render(request, 'location.html', {"images":images, "location":location})   

def search_category(request):

    location = Location.objects.all()

    if "gallery" in request.GET and request.GET["gallery"]:
        search_term = request.GET.get("gallery")
        searched= Image.search_by_category(search_term)
        message = f"{searched}"

        return render(request, 'search.html', {"message": message, "images": searched, "location":location})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html', {"message": message, "location":location})
