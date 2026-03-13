"""
populate_db.py - Script to populate Octofit Tracker database with test data using Django ORM
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Activity, Team

# Create test users
def create_users():
    users = [
        User(username='alice', email='alice@example.com'),
        User(username='bob', email='bob@example.com'),
        User(username='charlie', email='charlie@example.com'),
    ]
    for user in users:
        user.set_password('test1234')
        user.save()
    print('Test users created.')

# Create test teams
def create_teams():
    team1 = Team(name='Team Alpha')
    team2 = Team(name='Team Beta')
    team1.save()
    team2.save()
    print('Test teams created.')

# Create test activities
def create_activities():
    alice = User.objects.get(username='alice')
    bob = User.objects.get(username='bob')
    charlie = User.objects.get(username='charlie')
    activities = [
        Activity(user=alice, type='Running', duration=30, distance=5),
        Activity(user=bob, type='Cycling', duration=45, distance=15),
        Activity(user=charlie, type='Swimming', duration=20, distance=1),
    ]
    for activity in activities:
        activity.save()
    print('Test activities created.')

if __name__ == '__main__':
    create_users()
    create_teams()
    create_activities()
    print('Database populated with test data.')
