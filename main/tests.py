from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Habit
from users.models import User
from config.settings import TG_CHAT_ID


# Create your tests here.
class HabitTestcase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@yandex.ru',
            tg_chat_id=TG_CHAT_ID

        )
        self.user.set_password('12345678')
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {
                'email': 'test@yandex.ru',
                'password': '12345678',

            }
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit.objects.create(
            name='test1',
            owner=self.user,
            place='место',
            time='10:00',
            is_pleasurable=False,
            action='действие',
            periodic=1,
            reward='награда',
            execution_time='1:00'

        )

        self.second_habit = Habit.objects.create(
            name='test2',
            owner=self.user,
            place='место',
            time='10:00',
            is_pleasurable=False,
            action='действие',
            periodic=1,
            reward='награда',
            execution_time='1:00'
        )

    # def test_delete_habit(self):
    #     response = self.client.delete(
    #         '/habit/delete/5/'
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_204_NO_CONTENT
    #     )

    def test_habit_list(self):
        response = self.client.get(
            '/habit/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_create(self):
        response = self.client.post(
            '/habit/create/',

            name='test2',
            place='место',
            time='10:00',
            is_pleasurable=True,
            action='действие',
            periodic=1,
            reward='награда',
            execution_time='1:00'

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
