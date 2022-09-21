from django.test import Client, TestCase
from django.urls import resolve

# Create your tests here.
class MywatchlistTest(TestCase):
    def test_mywatchlist_show_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_mywatchlist_show_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_mywatchlist_show_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
