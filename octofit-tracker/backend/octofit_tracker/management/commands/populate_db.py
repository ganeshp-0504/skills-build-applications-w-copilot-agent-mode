from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='password1')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='password2')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='password3')

        # Teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Beta', members=[user3.email])

        # Activities
        Activity.objects.create(user=user1.email, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2.email, activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3.email, activity_type='strength', duration=20, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=team1.name, points=150)
        Leaderboard.objects.create(team=team2.name, points=100)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Running', description='Run for 15 minutes')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
