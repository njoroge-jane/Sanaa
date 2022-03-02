from django.test import TestCase

from album.models import Category, Image, Location
from album.views import location

# Create your tests here.


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.food= Category(category_name = 'Food')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category)) 
    # Test Save instance  
    def test_save(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0) 

    def test_delete_method(self):
        self.food.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)==0)         


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.diaspora= Location(location_name = 'Diaspora')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.diaspora,Location))

    def test_save(self):
        self.diaspora.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0) 

    def test_delete(self):
        self.diaspora.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)      

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.nairobi= Location(location_name = 'Food')
        self.nairobi.save_location()

        # Creating a new category and saving it
        self.new_category = Category(category_name = 'Travel')
        self.new_category.save()

        self.new_image= Image(title = 'Test',post = 'This is a random test Post',location= self.nairobi)
        self.new_image.save()

        self.new_image.category.add(self.new_category)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_search_by_category(self):
        self.new_image.save_image()
        images = Image.search_by_category(self.new_image.category)   
        self.assertTrue(len(images)>0)  
    
    def test_filter_by_location(self):
        self.new_image.save_image()
        images = Image.filter_by_location(self.new_image.location)   
        self.assertTrue(len(images)>0)             