from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date = time)


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        response = self.client.get(reversed('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
