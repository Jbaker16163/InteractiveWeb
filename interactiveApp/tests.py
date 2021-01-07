from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from interactiveApp.views import *
from django.template.loader import render_to_string
import interactiveApp

# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, 'Home page resolves incorrectly')

    def testHomePageInfo(self):
        request = HttpRequest()
        response = interactiveApp.views.home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html lang="en" id="css">'))
        self.assertIn('<title>Skelio Adventure</title>', html)
        self.assertTrue(html.endswith('</html>'))

class FirstPageTest(TestCase):

    def testFirstPage(self):
        found = resolve('/firstInteractive/')
        self.assertEqual(found.func, first_page, 'First page resolves incorrectly')

    def testFirstPageInfo(self):
        request = HttpRequest()
        response = interactiveApp.views.first_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html lang="en">'))
        self.assertIn('<title>Class Selection</title>', html)
        self.assertTrue(html.endswith('</html>'))

class SecondPageTest(TestCase):

    def testSecondPage(self):
        found = resolve('/secondInteractive/')
        self.assertEqual(found.func, second_page, 'Second page resolves incorrectly')

    def testSecondPageInfo(self):
        request = HttpRequest()
        response = interactiveApp.views.second_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html lang="en">'))
        self.assertIn('<title>Race Selection</title>', html)
        self.assertTrue(html.endswith('</html>'))


class ThirdPageTest(TestCase):

    def testThirdPage(self):
        found = resolve('/thirdInteractive/')
        self.assertEqual(found.func, third_page, 'Third page resolves incorrectly')

    def testThirdPageInfo(self):
        request = HttpRequest()
        response = interactiveApp.views.third_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html lang="en">'))
        self.assertIn('<title>Confirm Character</title>', html)
        self.assertTrue(html.endswith('</html>'))

class FourthPageTest(TestCase):

    def testFourthPage(self):
        found = resolve('/fourthInteractive/')
        self.assertEqual(found.func, fourth_page, 'Fourth page resolves incorrectly')

        def testFourthPageInfo(self):
            request = HttpRequest()
            response = interactiveApp.views.fourth_page(request)
            html = response.content.decode('utf8')
            self.assertTrue(html.startswith('<html lang="en">'))
            self.assertIn('<title>Location Selection</title>', html)
            self.assertTrue(html.endswith('</html>'))

class FifthPageTest(TestCase):

    def testFifthPage(self):
        found = resolve('/fifthInteractive/')
        self.assertEqual(found.func, fifth_page, 'Fifth page resolves incorrectly')

        def testFifthPageInfo(self):
            request = HttpRequest()
            response = interactiveApp.views.fourth_page(request)
            html = response.content.decode('utf8')
            self.assertTrue(html.startswith('<html lang="en">'))
            self.assertIn('<title>Starting Area</title>', html)
            self.assertTrue(html.endswith('</html>'))