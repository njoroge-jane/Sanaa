from django.db import models
import datetime as dt



# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=60) 
  
  def __str__(self):
        return self.location_name  

class Category(models.Model):
  category_name = models.CharField(max_length=60) 
  
  def __str__(self):
        return self.category_name          

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ManyToManyField(Location)   
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.title 

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news                   

