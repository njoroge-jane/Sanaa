from django.shortcuts import render,redirect
from django.http import HttpResponse

from album.models import Image,Category,Location

# Create your views here.
def index(request):
  images = Image.objects.all()
  return render(request,'index.html',{"images":images,})

def location(request):
  if location == 'nairobi':
    return redirect('nairobi.html')

  return render(request,'diaspora.html')    

