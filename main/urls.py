from main.apps import MainConfig
from django.urls import path
from main.views import HabitsViewSet, HabitsListView
from rest_framework.routers import DefaultRouter

app_name = MainConfig.name


router = DefaultRouter()
router.register(r'habits', HabitsViewSet, basename='habits')


urlpatterns = [
    path('public_habits/', HabitsListView.as_view(), name='habits_list'),
              ] + router.urls

