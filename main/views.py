from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import Habit
from main.paginators import HabitPagination
from main.permissions import HabitPermissions
from main.serializers import HabitSerializers
from main.tasks import send_tg_create_message


class HabitsCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        """Сохраняет новому объекту владельца
         и отправляет уведмоление в тг о создании"""
        serializer.save(owner=self.request.user)
        habit = serializer.save()
        send_tg_create_message(habit.id)


class HabitsListApiView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Список публичных привычек"""
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == 'moderators':
            return Habit.objects.all()
        else:
            queryset = (Habit.objects.filter(public=True)
                        | Habit.objects.filter(owner=user))
            return queryset


class HabitRetrieveApiView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = [HabitPermissions]


class HabitUpdateApiView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = [HabitPermissions]


class HabitDeleteApiView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializers
    permission_classes = [HabitPermissions]
