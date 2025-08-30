from rest_framework import viewsets
from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from pymongo import MongoClient
from rest_framework.response import Response
from rest_framework.views import APIView

# Helper to get MongoDB collection
client = MongoClient('localhost', 27017)
db = client['octofit_db']

class UsersViewSet(APIView):
    def get(self, request):
        users = list(db.users.find({}, {'_id': 0}))
        return Response(users)

class TeamsViewSet(APIView):
    def get(self, request):
        teams = list(db.teams.find({}, {'_id': 0}))
        return Response(teams)

class ActivitiesViewSet(APIView):
    def get(self, request):
        activities = list(db.activities.find({}, {'_id': 0}))
        return Response(activities)

class LeaderboardViewSet(APIView):
    def get(self, request):
        leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
        return Response(leaderboard)

class WorkoutsViewSet(APIView):
    def get(self, request):
        workouts = list(db.workouts.find({}, {'_id': 0}))
        return Response(workouts)

urlpatterns = [
    path('api/users/', UsersViewSet.as_view()),
    path('api/teams/', TeamsViewSet.as_view()),
    path('api/activities/', ActivitiesViewSet.as_view()),
    path('api/leaderboard/', LeaderboardViewSet.as_view()),
    path('api/workouts/', WorkoutsViewSet.as_view()),
]
