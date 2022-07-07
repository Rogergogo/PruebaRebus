from turtle import position
from django.db import models
from django.conf import settings
from .managers import PlayerManager, StaffManager


class Team(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(
        'Nombre',
        max_length=255
    )
    logo_image_b64 = models.BinaryField(blank=True, null=False)
    shield_image_b64 = models.BinaryField(blank=True, null=False)

    class Meta:
        db_table = 'Team'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.name


class Person(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(
        'Nombre',
        max_length=255
    )
    last_name = models.CharField(
        'Apellido',
        max_length=255
    )
    birthday = models.DateField()
    nationality = models.CharField(
        'Nacionalidad',
        max_length=255
    )

    class Meta:
        db_table = 'Person'
        verbose_name = 'Persona'
        verbose_name_plural = 'Persona'

    def __str__(self):
        return f'{self.name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


class Player(models.Model):

    POSITIONS = (
        ('Arquero', 'Arquero'),
        ('Defensa', 'Defensa'),
        ('Mediocampo', 'Mediocampo'),
        ('Delantero', 'Delantero'),
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    position = models.CharField(
        'Posicion',
        max_length=255,
        choices=POSITIONS
    )
    number = models.IntegerField(blank=True, null=True)
    starter = models.BooleanField(
        'Titular',
        default=False,
    )
    photo_image_b64 = models.BinaryField(blank=True, null=False)
    person = models.ForeignKey(
        Person,
        models.CASCADE,
        related_name='person_player',
        related_query_name='person_player',
        blank=False,
        null=False,
    )
    team = models.ForeignKey(
        Team,
        models.CASCADE,
        related_name='player_team',
        related_query_name='player_team',
        blank=False,
        null=False,
    )

    objects = PlayerManager()

    class Meta:
        db_table = 'Player'
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.person.name


class Staff(models.Model):

    ROLES = (
        ('Tecnico', 'Tecnico'),
        ('Asistencia', 'Asistencia'),
        ('Medico', 'Medico'),
        ('Preparador', 'Preparador'),
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    role = models.CharField(
        'Rol',
        max_length=255,
        choices=ROLES
    )
    person = models.ForeignKey(
        Person,
        models.CASCADE,
        related_name='person_staff',
        related_query_name='person_staff',
        blank=False,
        null=False,
    )
    team = models.ForeignKey(
        Team,
        models.CASCADE,
        related_name='staff_team',
        related_query_name='staff_team',
        blank=False,
        null=False,
    )

    objects = StaffManager()

    class Meta:
        db_table = 'Staff'

    def __str__(self):
        return self.person.name

