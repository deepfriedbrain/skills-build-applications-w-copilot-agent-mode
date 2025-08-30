
from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users (super heroes)
        users = [
            {'name': 'Tony Stark', 'email': 'tony@marvel.com', 'team': 'Marvel'},
            {'name': 'Steve Rogers', 'email': 'steve@marvel.com', 'team': 'Marvel'},
            {'name': 'Bruce Wayne', 'email': 'bruce@dc.com', 'team': 'DC'},
            {'name': 'Clark Kent', 'email': 'clark@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {'name': 'Marvel', 'members': ['tony@marvel.com', 'steve@marvel.com']},
            {'name': 'DC', 'members': ['bruce@dc.com', 'clark@dc.com']},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {'user_email': 'tony@marvel.com', 'type': 'running', 'points': 50},
            {'user_email': 'steve@marvel.com', 'type': 'walking', 'points': 30},
            {'user_email': 'bruce@dc.com', 'type': 'strength', 'points': 40},
            {'user_email': 'clark@dc.com', 'type': 'running', 'points': 60},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'Marvel', 'points': 80},
            {'team': 'DC', 'points': 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user_email': 'tony@marvel.com', 'workout': '5K run'},
            {'user_email': 'steve@marvel.com', 'workout': 'Yoga'},
            {'user_email': 'bruce@dc.com', 'workout': 'Weightlifting'},
            {'user_email': 'clark@dc.com', 'workout': 'Sprints'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
