from rest_framework import serializers
from main.models import Habit
from main.validators import excludeValidator


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [excludeValidator]
