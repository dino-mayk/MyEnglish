from django.shortcuts import reverse
from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_translator_endpoint(self):
        with self.subTest('there is a translator.'):
            response = Client().get(reverse('translator:index'))
            self.assertEqual(response.status_code, 200)
