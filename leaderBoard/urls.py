from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='Home'),
    path('current-week-leaderboard/', current_week_leaderboard, name='current_week_leaderboard'),
    path('last-week-leaderboard/', last_week_leaderboard, name='last_week_leaderboard'),
    path('user-rank/', user_rank, name='user_rank'),
]