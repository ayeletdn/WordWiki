from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class TestFatherSon(TestCase):
    def test_calc(self):
        c = Client()
        d = dict(
            father_name="Abraham",
            son_name="Izzac",
            father_year=1900,
            son_year=1935,
        )
        response = c.post(reverse('fatherson:calc'), d)
        self.assertEqual(200, response.status_code)
        c = response.context
        self.assertEqual(d['father_name'], c['father_name'])
        self.assertEqual(d['son_name'], c['son_name'])
        self.assertEqual(70, c['father_age'])
        self.assertEqual(35, c['son_age'])
        self.assertContains(response, r'')