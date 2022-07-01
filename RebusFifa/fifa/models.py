from turtle import position
from django.db import models
from django.conf import settings


POSITIONS = (
    ("Arquero", "Arquero"),
    ("Defensa", "Defensa"),
    ("Mediocampo", "Mediocampo"),
    ("Delantero", "Delantero"),
)

ROLS = (
    ("Tecnico", "Tecnico"),
    ("Asistencia", "Asistencia"),
    ("Medico", "Medico"),
    ("Preparador", "Preparador"),
)


class Team(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=False)
    name = models.CharField(
        "Nombre",
        max_length=255
    )
    logo_image_b64 = models.BinaryField(blank=True, null=False)
    shield_image_b64 = models.BinaryField(blank=True, null=False)


class Player(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=False)
    name = models.CharField(
        "Nombre",
        max_length=255
    )
    last_name = models.CharField(
        "Apellido",
        max_length=255
    )
    birthday = models.DateField()
    position = models.CharField(
        "Posicion",
        max_length=255,
        choices=POSITIONS
    )
    number = models.IntegerField(blank=True, null=True)
    starter = models.BooleanField(
        "Titular",
        default=False,
    )
    photo_image_b64 = models.BinaryField(blank=True, null=False)


class Staff(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=False)
    name = models.CharField(
        "Nombre",
        max_length=255
    )
    last_name = models.CharField(
        "Apellido",
        max_length=255
    )
    birthday = models.DateField()
    nationality = models.CharField(
        "Nacionalidad",
        max_length=255
    )
    role = models.CharField(
        "Rol",
        max_length=255,
        choices=ROLS
    )

