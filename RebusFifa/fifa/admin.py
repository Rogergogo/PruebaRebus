from django.contrib import admin
from .models import Team, Person, Player, Staff


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 'updated_at')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 'updated_at')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 'updated_at')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 'updated_at')

