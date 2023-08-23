from main.apps import MainConfig
from main.views import (HabitsListApiView, HabitsCreateApiView,
                        HabitRetrieveApiView, HabitUpdateApiView, HabitDeleteApiView)
from django.urls import path

app_name = MainConfig.name


urlpatterns = [
    path('', HabitsListApiView.as_view()),
    path('create/', HabitsCreateApiView.as_view()),
    path('detail/<int:pk>/', HabitRetrieveApiView.as_view()),
    path('update/<int:pk>/', HabitUpdateApiView.as_view()),
    path('delete/<int:pk>/', HabitDeleteApiView.as_view())
]
