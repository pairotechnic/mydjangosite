'''
    Purpose : Tests that ensure the application behaves as intended
    Author : Rohit Pai
    Date : 17th July 2024
'''

# Standard Library Imports
import datetime

# Third Party Imports
from django.test import TestCase
from django.utils import timezone

# Local Application Imports
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
            was_published_recently() returns False for questions whose pub_date is in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
