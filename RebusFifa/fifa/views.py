from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Person, Team, Player, Staff


@api_view(['GET'])
@renderer_classes([JSONRenderer])  
def stats(request):
    """Api Statistics Fifa"""
    
    content = {
        'total_teams': Team.objects.count(),
        'total_players': Player.objects.count(),
        'youngest_player': Player.objects.youngest().person.name,
        'oldest_player': Player.objects.oldest().person.name,
        'total_not_starter_players': Player.objects.count_not_starters(),
        'avg_not_starter_players': Player.objects.avg_not_starter(),
        'highest_players_registered_team': Player.objects.highest_players_registered_team(),
        'avg_age': Player.objects.avg_age(),
        'avg_players_team': Player.objects.avg_x_team(),
        'oldest_staff': Staff.objects.oldest().person.name
    }

    return Response(content)
       