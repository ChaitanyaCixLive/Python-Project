from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pub_date = time)
        self.assertIs(futureQuestion.was_published_recently(), False)
