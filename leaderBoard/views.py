
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Leaderboard
from django.shortcuts import render

def current_week_leaderboard(request):

    start_of_week = timezone.now() - timedelta(days=timezone.now().weekday())
    leaderboard = Leaderboard.objects.filter(timestamp__gte=start_of_week).order_by('-score')[:200]
    data = [{'UID': entry.UID, 'name': entry.name, 'score': entry.score, 'country': entry.country} for entry in leaderboard]
    return render(request, 'HomePage.html', {'leaderboard': data})

def last_week_leaderboard(request):

    start_of_last_week = timezone.now() - timedelta(days=timezone.now().weekday() + 7)
    end_of_last_week = start_of_last_week + timedelta(days=7)
    country = request.GET.get('country')  # Get country from user input
    leaderboard = Leaderboard.objects.filter(timestamp__range=(start_of_last_week, end_of_last_week), country=country).order_by('-score')[:200]
    data = [{'UID': entry.UID, 'name': entry.name, 'score': entry.score, 'country': entry.country} for entry in leaderboard]
    return render(request, 'HomePage.html', {'leaderboard': data})

def user_rank(request):
    user_id = request.GET.get('user_id')
    user_entry = Leaderboard.objects.filter(UID=user_id).first()
    if user_entry:
        # Get rank of the user based on the score
        rank = Leaderboard.objects.filter(score__gt=user_entry.score).count() + 1
        data = [{'UID': user_entry.UID, 'name': user_entry.name, 'score': user_entry.score, 'country': user_entry.country, 'rank': rank}]

        return render(request, 'HomePage.html', {'leaderboard': data})
    else:
        return JsonResponse({'error': 'User not found'})


def home_view(request):

    leaderboard = Leaderboard.objects.all()  # Fetch the leaderboard data as needed
    data = [{'UID': entry.UID, 'name': entry.name, 'score': entry.score, 'country': entry.country} for entry in leaderboard]
    return render(request, 'HomePage.html', {'leaderboard': data})

