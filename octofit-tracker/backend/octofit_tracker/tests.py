from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Run', user_email='test@example.com', team='Test Team')
        self.assertEqual(str(activity), 'Run - test@example.com')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', team='Test Team', score=10)
        self.assertEqual(str(lb), 'test@example.com - 10')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 10 pushups')
        self.assertEqual(str(workout), 'Pushups')
