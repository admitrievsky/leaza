from calendar import mdays
from datetime import datetime, timedelta, timezone

from django.test import TestCase
from .plural_rus import time_elapsed, get_comment_count


class PluralTestCase(TestCase):
    def setUp(self):
        pass

    def test_time_elapsed(self):
        now = datetime.now(timezone.utc)
        self.assertEquals(time_elapsed(now - timedelta(0)), '0 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=1)), '1 минуту')
        self.assertEquals(time_elapsed(now - timedelta(minutes=2)), '2 минуты')
        self.assertEquals(time_elapsed(now - timedelta(minutes=3)), '3 минуты')
        self.assertEquals(time_elapsed(now - timedelta(minutes=4)), '4 минуты')
        self.assertEquals(time_elapsed(now - timedelta(minutes=5)), '5 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=6)), '6 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=7)), '7 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=8)), '8 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=9)), '9 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=10)), '10 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=11)), '11 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=12)), '12 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=13)), '13 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=14)), '14 минут')
        self.assertEquals(time_elapsed(now - timedelta(minutes=15)), '15 минут')

        self.assertEquals(time_elapsed(now - timedelta(minutes=59)), '59 минут')
        self.assertEquals(time_elapsed(now - timedelta(hours=1)), '1 час')
        self.assertEquals(time_elapsed(now - timedelta(hours=2)), '2 часа')
        self.assertEquals(time_elapsed(now - timedelta(hours=3)), '3 часа')
        self.assertEquals(time_elapsed(now - timedelta(hours=4)), '4 часа')
        self.assertEquals(time_elapsed(now - timedelta(hours=5)), '5 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=6)), '6 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=7)), '7 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=8)), '8 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=9)), '9 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=10)), '10 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=11)), '11 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=12)), '12 часов')
        self.assertEquals(time_elapsed(now - timedelta(hours=13)), '13 часов')

        self.assertEquals(time_elapsed(now - timedelta(hours=23)), '23 часа')
        self.assertEquals(time_elapsed(now - timedelta(days=1)), '1 день')
        self.assertEquals(time_elapsed(now - timedelta(days=2)), '2 дня')
        self.assertEquals(time_elapsed(now - timedelta(days=3)), '3 дня')
        self.assertEquals(time_elapsed(now - timedelta(days=4)), '4 дня')
        self.assertEquals(time_elapsed(now - timedelta(days=5)), '5 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=6)), '6 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=7)), '7 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=8)), '8 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=9)), '9 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=10)), '10 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=11)), '11 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=12)), '12 дней')

        self.assertEquals(time_elapsed(now - timedelta(days=30)), '30 дней')
        self.assertEquals(time_elapsed(now - timedelta(days=31)), '31 день')
        self.assertEquals(time_elapsed(now - timedelta(days=32)), '1 месяц')

    def test_comment_count(self):
        self.assertEquals(get_comment_count(0), '0 комментариев')
        self.assertEquals(get_comment_count(1), '1 комментарий')
        self.assertEquals(get_comment_count(2), '2 комментария')
        self.assertEquals(get_comment_count(3), '3 комментария')
        self.assertEquals(get_comment_count(4), '4 комментария')
        self.assertEquals(get_comment_count(5), '5 комментариев')
        self.assertEquals(get_comment_count(6), '6 комментариев')
        self.assertEquals(get_comment_count(7), '7 комментариев')
        self.assertEquals(get_comment_count(8), '8 комментариев')
        self.assertEquals(get_comment_count(9), '9 комментариев')
        self.assertEquals(get_comment_count(10), '10 комментариев')
        self.assertEquals(get_comment_count(11), '11 комментариев')