from django.urls import path, include
from .views import stats

urlpatterns = [
    path('fifa/stats', stats, name='fifa-stats'),
]
