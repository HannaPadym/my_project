from django.test import TestCase
from .views import signs


# Create your tests here.
class TestHoroscope(TestCase):
    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
                      response.content.decode())

    def test_signs(self):
        for k, v in signs.items():
            response = self.client.get(f'/horoscope/{k}/')
            self.assertIn(v, response.content.decode())

    def test_redirect(self):
        signs_lst = list(signs)
        for i in range(1, 13):
            response = self.client.get(f'/horoscope/{i}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{signs_lst[i - 1]}/')
