from django.test import TestCase

from album.models import Category, Image, Location

# Create your tests here.


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.food= Category(category_name = 'Food')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))    


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.diaspora= Location(location_name = 'Diaspora')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.diaspora,Location))

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