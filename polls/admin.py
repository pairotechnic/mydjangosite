'''
    Purpose : Register models to have an admin interface
    Author : Rohit Pai
    Date : 14th July 2024
'''

# Standard Library Imports

# Third Party Imports
from django.contrib import admin

# Local Application Imports
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields=["pub_date", "question_text"]

admin.site.register(Question, QuestionAdmin)
