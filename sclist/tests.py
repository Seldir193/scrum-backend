# tests.py
from django.test import TestCase
from .models import Contact
# tests.py

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase

from django.test import TestCase
from .models import Task, CustomUser


class ContactModelTest(TestCase):

    def setUp(self):
        # Ändere 'phone_number' zu 'phoneNumber' wie im Modell
        self.contact = Contact.objects.create(
            name="John Doe", 
            email="johndoe@example.com", 
            phoneNumber="1234567890"  # Korrektes Feldname
        )

    def test_contact_creation(self):
        # Teste, ob der Kontakt korrekt erstellt wurde
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.email, "johndoe@example.com")
        self.assertEqual(self.contact.phoneNumber, "1234567890")  # Korrektes Feldname

    def test_contact_str(self):
        # Teste die __str__ Methode
        self.assertEqual(str(self.contact), "John Doe")







class TaskViewSetTest(APITestCase):
    def setUp(self):
        # Verwende get_user_model, um CustomUser zu erhalten
        User = get_user_model()  
        self.user = User.objects.create_user(username='testuser', password='password')
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)






class TaskModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.task = Task.objects.create(
            user=self.user,
            text='Sample Task',
            description='Task description',
            status='todos'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.text, 'Sample Task')
        self.assertEqual(self.task.status, 'todos')

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Sample Task (To Do)')









