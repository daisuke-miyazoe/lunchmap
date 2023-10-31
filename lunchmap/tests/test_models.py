from django.test import TestCase
from ..models import Category


class CategoryModelTest(TestCase):
    def test_is_empty(self):
        category = Category.objects.all()
        self.assertEqual(category.count(), 0)
