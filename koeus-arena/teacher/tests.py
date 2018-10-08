from django.test import TestCase
from teacher.models import Account, AccountManager, Classroom, Student
# from teacher.forms import SignupForm
from teacher import views
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class AccountTest(TestCase):
	def create_account(self,  email = 'myemail@gmail.com', firstName = 'first', lastName = 'last'):
		return Account.objects.create_user(email = email, firstName = firstName, lastName = lastName)
	def test_account_creation_shouldpass(self):
		account = self.create_account()
		self.assertTrue(isinstance(account, Account))
	def test_account_email(self):
		account = self.create_account()
		self.assertEqual(account.__str__(), account.email)
	def test_account_lastname(self):
		account = self.create_account()
		self.assertEqual(account.getLastName(), account.lastName)
class TeacherHomeTests(SimpleTestCase):

    def test_teacherhome_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('teacher'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('teacher'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/teacherHome.html')
    def test_teacherhome_page_contains_correct_html(self):
        response = self.client.get('/home/')
        self.assertContains(response, ' <title>Teacher Dashboard</title>')
    def test_teacherhome_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/home/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

class StudentHomeTests(SimpleTestCase):

    def test_studenthome_page_status_code(self):
        response = self.client.get('/student/')
        self.assertEquals(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('student'))
        self.assertEquals(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/studentHome.html')
    def test_studenthome_page_contains_correct_html(self):
        response = self.client.get('/student/')
        self.assertContains(response, ' <title>Student Page</title>')
    def test_studenthome_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/student/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

class RoomViewTests(SimpleTestCase):

    def test_room_page_status_code(self):
        response = self.client.get('/room/')
        self.assertEquals(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('room'))
        self.assertEquals(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('room'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/room.html')
    def test_room_page_contains_correct_html(self):
        response = self.client.get('/room/')
        self.assertContains(response, '<title>Room</title>')
    def test_room_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/room/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

class CookieTests(SimpleTestCase):

    def test_cookie_page_status_code(self):
        response = self.client.get('/cookie/')
        self.assertEquals(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('cookie'))
        self.assertEquals(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cookie'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/cookie.html')
    def test_cookie_page_contains_correct_html(self):
        response = self.client.get('/cookie/')
        self.assertContains(response, '<title>Competition</title>')
    def test_cookie_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/cookie/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

class LeaderBoardTests(SimpleTestCase):

    def test_leaderBoard_page_status_code(self):
        response = self.client.get('/leader/')
        self.assertEquals(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('leader'))
        self.assertEquals(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('leader'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/leaderboard.html')
    def test_leaderBoard_page_contains_correct_html(self):
        response = self.client.get('/leader/')
        self.assertContains(response, '<h1>Leaderboard does not currently exist...</h1>')
    def test_leaderBoard_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/leader/')
        self.assertNotContains(
            response, '<h1>Leaderboard does currently exist!!!</h1>')

class LoginViewTests(SimpleTestCase):

    def test_login_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
    def test_login_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Log In</title>')
    def test_login_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, '<h1>This is definitely not the log in page</h1>')
