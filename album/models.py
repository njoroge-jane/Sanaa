from email.mime import image
from django.db import models
import datetime as dt



# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=60) 
  
  def __str__(self):
        return self.location_name
  def save_location(self):   
        self.save()         

class Category(models.Model):
  category_name = models.CharField(max_length=60) 
  
  def __str__(self):
        return self.category_name  
  def save_category(self):   
        self.save()               

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.title 

    @classmethod
    def search_by_category(cls,search_term):
        post = cls.objects.filter(category__icontains=search_term)
        return post  

    def save_image(self):   
        self.save()  

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id = id)
        return image                  

