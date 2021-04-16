  
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
User=get_user_model()
# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        user_a_pass ='amira12234'
        self.user_a_pass=user_a_pass
        user_a = User(username='amira', email='amira@amira.com')
        user_a.is_staff= True
        user_a.is_superuser = True
        user_a.set_password(user_a_pass)
        user_a.save()
        self.user_a = user_a
    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count,1)#user_count == 1
        self.assertNotEqual(user_count,0) #!=
    def test_password(self):
        user_a=User.objects.get(username="amira")
        self.assertTrue(user_a.check_password(self.user_a_pass))
    def test_login_url(self):
        login_url = settings.LOGIN_URL
        data = {"username":"amira", "password":self.user_a_pass}
        #response = self.client.post(url, {}, follow=True)
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(status_code, 200)        