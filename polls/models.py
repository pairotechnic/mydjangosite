'''
    Purpose : Defines all the models in the polls app
    Author : Rohit Pai
    Date : 13th July 2024

    NOTE : 
    Models represent database tables.
    The fields in models represent the columns in database tables.
'''

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
