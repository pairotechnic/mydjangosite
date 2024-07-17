'''
    Purpose : Defines all the models in the polls app
    Author : Rohit Pai
    Date : 13th July 2024

    NOTE : 
    Models represent database tables.
    The fields in models represent the columns in database tables.
'''

# Standard Library Imports
import datetime

# Third Party Imports
from django.db import models
from django.utils import timezone

# Local Application Imports


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
