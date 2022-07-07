from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker
from .models import Team, Player, Staff, Person


class AccountTests(APITestCase):
    def setUp(self):
        fake = Faker(['es_CO'])

        team = Team.objects.create(
            name="America",
            logo_image_b64=fake.binary(length=255),
            shield_image_b64=fake.binary(length=255)
        )

        person_player = Person.objects.create(
            name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=fake.date_between(
                start_date=datetime(1990, 1, 1),
                end_date=datetime(2000, 1, 1)
            ))

        person_staff = Person.objects.create(
            name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=fake.date_between(
                start_date=datetime(1970, 1, 1),
                end_date=datetime(1990, 1, 1)
            ))

        Player.objects.create(
            position="Delantero",
            number=1,
            starter=True,
            photo_image_b64=fake.binary(length=255),
            person=person_player,
            team=team
        )

        Staff.objects.create(
            role="Tecnico",
            team=team,
            person=person_staff
        )

    def test_response_api(self):
        """
        Test Api
        """
        url = reverse('fifa-stats')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        print(response.data)
