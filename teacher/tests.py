from django.test import TestCase
from teacher.models import Account, AccountManager, Classroom, Student
# from teacher.forms import SignupForm
from teacher import views
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from django.test import LiveServerTestCase
import unittest, time, re


class ASignUpTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_a_sign_up(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::button[1]"
        ).click()
        driver.find_element_by_id("id_email").click()
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("newUser@mail.com")
        driver.find_element_by_id("id_firstName").click()
        driver.find_element_by_id("id_firstName").clear()
        driver.find_element_by_id("id_firstName").send_keys("first")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Email:'])[1]/following::p[1]"
        ).click()
        driver.find_element_by_id("id_lastName").click()
        driver.find_element_by_id("id_lastName").clear()
        driver.find_element_by_id("id_lastName").send_keys("last")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='FirstName:'])[1]/following::p[1]"
        ).click()
        driver.find_element_by_id("id_password1").click()
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("password1234")
        driver.find_element_by_id("id_password2").click()
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("password1234")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password2:'])[1]/following::button[1]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class TeacherLoginUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_teacher_login_unit(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("newUser@mail.com")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password1234")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class AddStudent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_student(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("newUser@mail.com")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password1234")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]"
        ).click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total Students:'])[1]/following::i[1]"
        ).click()
        driver.find_element_by_id("id_lastName").click()
        driver.find_element_by_id("id_lastName").clear()
        driver.find_element_by_id("id_lastName").send_keys("lastname")
        driver.find_element_by_id("id_firstName").click()
        driver.find_element_by_id("id_firstName").clear()
        driver.find_element_by_id("id_firstName").send_keys("firstname")
        driver.find_element_by_id("id_studentNumber").click()
        driver.find_element_by_id("id_studentNumber").click()
        driver.find_element_by_id("id_studentNumber").clear()
        driver.find_element_by_id("id_studentNumber").send_keys("245789099")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='delete'])[1]/following::button[1]"
        ).click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[1]/following::button[1]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class AddStudentLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_student_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_id("id_teacherEmail").click()
        driver.find_element_by_id("id_teacherEmail").clear()
        driver.find_element_by_id("id_teacherEmail").send_keys(
            "newUser@mail.com")
        driver.find_element_by_id("id_firstName").click()
        driver.find_element_by_id("id_firstName").clear()
        driver.find_element_by_id("id_firstName").send_keys("firstname")
        driver.find_element_by_id("tab-item-1").click()
        driver.find_element_by_id("id_teacherEmail").click()
        driver.find_element_by_id("id_teacherEmail").clear()
        driver.find_element_by_id("id_teacherEmail").send_keys(
            "newUser@mail.com")
        driver.find_element_by_id("id_firstName").click()
        driver.find_element_by_id("id_firstName").clear()
        driver.find_element_by_id("id_firstName").send_keys("firstname")
        driver.find_element_by_id("id_lastName").click()
        driver.find_element_by_id("id_lastName").clear()
        driver.find_element_by_id("id_lastName").send_keys("lastname")
        driver.find_element_by_id("id_studentNumber").click()
        driver.find_element_by_id("id_studentNumber").click()
        driver.find_element_by_id("id_studentNumber").clear()
        driver.find_element_by_id("id_studentNumber").send_keys("245789099")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Studentnumber:'])[1]/following::input[2]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class NewRoomEdit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_open_room_to_edit(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("newUser@mail.com")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password1234")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]"
        ).click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total Students:'])[1]/following::i[1]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class AddNewRoomTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_new_room(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("newUser@mail.com")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password1234")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]"
        ).click()
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("create new room")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='create new room'])[1]/preceding::button[1]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class NewRoomUndo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_new_room_undo(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("newUser@mail.com")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password1234")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]"
        ).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


# Create your tests here.
class AccountTest(TestCase):

    def create_account(self,
                       email='myemail@gmail.com',
                       firstName='first',
                       lastName='last'):
        return Account.objects.create_user(
            email=email, firstName=firstName, lastName=lastName)

    def test_account_creation_shouldpass(self):
        account = self.create_account()
        self.assertTrue(isinstance(account, Account))

    def test_account_email(self):
        account = self.create_account()
        self.assertEqual(account.__str__(), account.email)

    def test_account_lastname(self):
        account = self.create_account()
        self.assertEqual(account.getLastName(), account.lastName)


# class TeacherHomeTests(SimpleTestCase):
#
#     def test_teacherhome_page_status_code(self):
#         response = self.client.get('/home/')
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('teacher'))
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('teacher'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/teacherHome.html')
#     def test_teacherhome_page_contains_correct_html(self):
#         response = self.client.get('/home/')
#         self.assertContains(response, ' <title>Teacher Dashboard</title>')
#     def test_teacherhome_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/home/')
#         self.assertNotContains(
#             response, 'Hi there! I should not be on the page.')
#
# class StudentHomeTests(SimpleTestCase):
#
#     def test_studenthome_page_status_code(self):
#         response = self.client.get('/student/')
#         self.assertEquals(response.status_code, 200)
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('student'))
#         self.assertEquals(response.status_code, 200)
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('student'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/studentHome.html')
#     def test_studenthome_page_contains_correct_html(self):
#         response = self.client.get('/student/')
#         self.assertContains(response, ' <title>Student Page</title>')
#     def test_studenthome_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/student/')
#         self.assertNotContains(
#             response, 'Hi there! I should not be on the page.')
#
# class RoomViewTests(SimpleTestCase):
#
#     def test_room_page_status_code(self):
#         response = self.client.get('/room/')
#         self.assertEquals(response.status_code, 200)
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('room'))
#         self.assertEquals(response.status_code, 200)
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('room'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/room.html')
#     def test_room_page_contains_correct_html(self):
#         response = self.client.get('/room/')
#         self.assertContains(response, '<title>Room</title>')
#     def test_room_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/room/')
#         self.assertNotContains(
#             response, 'Hi there! I should not be on the page.')

# class CookieTests(SimpleTestCase):
#
#     def test_cookie_page_status_code(self):
#         response = self.client.get('/cookie/')
#         self.assertEquals(response.status_code, 200)
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('lobby'))
#         self.assertEquals(response.status_code, 200)
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('lobby'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/cookie.html')
#     def test_cookie_page_contains_correct_html(self):
#         response = self.client.get('/cookie/')
#         self.assertContains(response, '<title>Competition</title>')
#     def test_cookie_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/cookie/')
#         self.assertNotContains(
#             response, 'Hi there! I should not be on the page.')
#
# class LeaderBoardTests(SimpleTestCase):
#
#     def test_leaderBoard_page_status_code(self):
#         response = self.client.get('/leader/')
#         self.assertEquals(response.status_code, 200)
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('leader'))
#         self.assertEquals(response.status_code, 200)
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('leader'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/leaderboard.html')
#     def test_leaderBoard_page_contains_correct_html(self):
#         response = self.client.get('/leader/')
#         self.assertContains(response, '<h1>Leaderboard does not currently exist...</h1>')
#     def test_leaderBoard_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/leader/')
#         self.assertNotContains(
#             response, '<h1>Leaderboard does currently exist!!!</h1>')
#
# class LoginViewTests(SimpleTestCase):
#
#     def test_login_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEquals(response.status_code, 200)
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('login'))
#         self.assertEquals(response.status_code, 200)
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('login'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/login.html')
#     def test_login_page_contains_correct_html(self):
#         response = self.client.get('/')
#         self.assertContains(response, '<title>Log In</title>')
#     def test_login_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/')
#         self.assertNotContains(
#             response, '<h1>This is definitely not the log in page</h1>')
