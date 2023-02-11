from django.test import TestCase
from restaurant.models import MenuItem

# Create your tests here.
class MenuItemTest(TestCase):

    def test_item(self):
        item = MenuItem.objects.create(
            title = 'Pizza',
            price = 20,
            inventory = 10
        )
        all_item = item.get_item()

        self.assertEqual(all_item, 'Pizza : 20')