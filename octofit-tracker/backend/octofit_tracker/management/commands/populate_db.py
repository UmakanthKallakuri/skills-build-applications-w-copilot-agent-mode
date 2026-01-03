from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import settings

# Define models for demonstration (replace with real models in production)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            {'email': 'tony@marvel.com', 'username': 'IronMan', 'team': marvel},
            {'email': 'steve@marvel.com', 'username': 'CaptainAmerica', 'team': marvel},
            {'email': 'bruce@marvel.com', 'username': 'Hulk', 'team': marvel},
            {'email': 'clark@dc.com', 'username': 'Superman', 'team': dc},
            {'email': 'bruce@dc.com', 'username': 'Batman', 'team': dc},
            {'email': 'diana@dc.com', 'username': 'WonderWoman', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = User.objects.create_user(email=u['email'], username=u['username'], password='password')
            user_objs.append(user)

        # Create activities
        Activity.objects.create(name='Running', user_email='tony@marvel.com', team='Marvel')
        Activity.objects.create(name='Swimming', user_email='clark@dc.com', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(user_email='tony@marvel.com', team='Marvel', score=100)
        Leaderboard.objects.create(user_email='clark@dc.com', team='DC', score=90)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups')
        Workout.objects.create(name='Situps', description='Do 50 situps')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
