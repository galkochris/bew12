from django.test import TestCase
from django.contrib.auth.models import User
from pets.models import Pet, Appointment
from django.urls import reverse



class PetsListTest(TestCase):
    def test_pet_list_page(self):
        response = self.client.get(reverse('pets:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no pets to display')
class PetDetailTest(TestCase):
    def test_pet_detail(self):
        user=User.objects.create_user(username='me', password='djangopony')
        self.client.login(username='me', password='djangopony')

        pet = Pet.objects.create(name="doug", breed="test", species="test", weight_in_pounds='123', owner=user)
        pet.save()

        response = self.client.get(reverse('pet:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'doug')
class PetCreationTest(TestCase):
    def test_pet_creation(self):
        user=User.objects.create_user(username='me', password='djangopony')
        self.client.login(username='me', password='djangopony')

        pet = Pet.objects.create(name="doug", breed="test", species="test", weight_in_pounds='123', owner=user)
        pet.save()

        response = self.client.post('/pets/create/', pet)
        updated = Pet.objects.get(name = pet['doug'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated.name, pet['doug'])
class AppointmentCreationTest(TestCase):
    def test_appointment_creation(self):
        user=User.objects.create_user(username='me', password='djangopony')
        self.client.login(username='me', password='djangopony')

        pet = Pet.objects.create(name="doug", breed="test", species="test", weight_in_pounds='123', owner=user)
        pet.save()
        event = Appointment.objects.create(date_of_appointment='2020-05-15', duration_minutes='30', pet=pet)
        event.save()

        response = self.client.post('/pets/create/', pet)
        updated = Appointment.objects.get(pet = pet['doug'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated.pet, pet['doug'])