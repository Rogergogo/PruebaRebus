import random
from datetime import datetime
from faker import Faker, providers
from django.core.management.base import BaseCommand

from ...models import Person, Team, Player, Staff

TEAMS = [
    'Atlético Nacional',
    'Millonarios',
    'Independiente Santa Fe',
    'América de Cali',
    'Cortuluá',
    'Junior de Barranquilla',
    'Deportivo Cali',
    'Independiente Medellín',
    'Once Caldas',
    'Deportes Tolima',
    'Deportivo Pasto'
]

POSITIONS = [
    'Arquero',
    'Defensa',
    'Mediocampo',
    'Delantero',
]

ROLES = [
    'Tecnico',
    'Asistencia',
    'Medico',
    'Preparador'
]


class Provider(providers.BaseProvider):
    def teams_name(self):
        return self.random_element(TEAMS)

    def player_position(self):
        return self.random_element(POSITIONS)

    def staff_rols(self):
        return self.random_element(ROLES)


class Command(BaseCommand):
    help = 'Comando para generar data fake en la db'

    def handle(self, *args, **kwargs):

        fake = Faker(['es_CO'])
        fake.add_provider(Provider)

        for _ in range(11):
            name = fake.unique.teams_name()
            Team.objects.create(
                name=name,
                logo_image_b64=fake.binary(length=255),
                shield_image_b64=fake.binary(length=255)
            )

        for _ in range(200):
            fake_person = Person.objects.create(
                name=fake.first_name(),
                last_name=fake.last_name(),
                birthday=fake.date_between(
                    start_date=datetime(1990, 1, 1),
                    end_date=datetime(2000, 1, 1)
                ),
            )

            Player.objects.create(
                position=fake.player_position(),
                number=random.randint(2, 99),
                starter=fake.boolean(chance_of_getting_true=75),
                photo_image_b64=fake.binary(length=255),
                person=fake_person,
                team_id=random.randint(1, 15)
            )

        for _ in range(50):
            fake_person = Person.objects.create(
                name=fake.first_name(),
                last_name=fake.last_name(),
                birthday=fake.date_between(
                    start_date=datetime(1980, 1, 1),
                    end_date=datetime(2000, 1, 1)
                ),
                nationality=fake.country()
            )

            Staff.objects.create(
                role=fake.staff_rols(),
                team_id=random.randint(1, 15),
                person=fake_person
            )
