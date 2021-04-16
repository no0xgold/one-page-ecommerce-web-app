from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase

# Create your tests here.
from .models import Product
User = get_user_model()

class ProductTestCase(TestCase):
    def setUp(self):
        user_a_pass ='amira122345'
        self.user_a_pass=user_a_pass
        user_a = User(username='amira1', email='amira1@amira1.com')
        user_a.is_staff= True
        user_a.is_superuser = False
        user_a.set_password(user_a_pass)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', "user2@user2.com", 'user21234')
        self.user_b = user_b

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count,2)

    def test_invalid_request(self):
        self.client.login(username=self.user_b, password='user21234')
        response = self.client.post("/products/create/", 
        {'title':'SayHello', 'dicription':'this is note for me',
        'price':'111'})
        self.assertTrue(response.status_code!=200)
    
    def test_valid_request(self):
        self.client.login(username=self.user_a, password="amira122345")
        response = self.client.post("/products/create/", 
        {'title':'SayHello', 'dicription':'this is note for me'})
        self.assertEqual(response.status_code,200)
