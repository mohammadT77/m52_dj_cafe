from django.test import TestCase

# Create your tests here.
from .models import MenuItem


class MenuItemTest(TestCase):

    def setUp(self) -> None:
        self.menu_item1 = MenuItem.objects.create(
            name='MenuItem1',
            price=1000,
            category='CatTest1',
            discount=20,  # percent
            image=None,
        )
        self.menu_item2 = MenuItem.objects.create(
            name='MenuItem2',
            price=2000,
            category='CatTest1',
            discount=None,  # percent
            image=None,
        )
        self.menu_item3 = MenuItem.objects.create(
            name='MenuItem3',
            price=3000,
            category='CatTest2',
            discount=10,  # percent
            image=None,
        )

    def test1_final_price(self):
        self.assertEqual(self.menu_item1.final_price(), 800)

    def test2_final_price(self):
        self.assertEqual(self.menu_item2.final_price(), 2000)

    def test3_final_price(self):
        self.assertEqual(self.menu_item3.final_price(), 3000-300)
