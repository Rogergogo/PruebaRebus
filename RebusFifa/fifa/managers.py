from django.db import models
from django.db.models import Max, Avg , F, Count
from datetime import date


class PlayerManager(models.Manager):
    def youngest(self):
        """Return the youngest player"""
        return self.get_queryset().order_by('-person__birthday').first()

    def oldest(self):
        """Return the oldest player"""       
        return self.get_queryset().order_by('person__birthday').first()

    def count_not_starters(self):
        return self.get_queryset().filter(starter=False).count()

    def highest_players_registered_team(self):
        return self.get_queryset().values_list('team__name').annotate(
                count_players=Count('id')
            ).order_by('-count_players').first()[0]

    def avg_not_starter(self):
        return self.get_queryset().filter(starter=False).values('team__name').annotate(
                count_not_starters=Count('id')
            ).aggregate(Avg('count_not_starters'))

    def avg_age(self):
        return self.get_queryset().annotate(
                age=(date.today().year-F('person__birthday__year'))
            ).aggregate(Avg('age'))['age__avg']

    def avg_x_team(self):
        return self.get_queryset().values('team__name').annotate(
                count_players=Count('id')
            ).aggregate(Avg('count_players'))


class StaffManager(models.Manager):
    def oldest(self):
        return self.get_queryset().order_by('person__birthday').first()

