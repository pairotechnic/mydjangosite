'''
    Purpose : Register models to have an admin interface
    Author : Rohit Pai
    Date : 14th July 2024
'''

# Standard Library Imports

# Third Party Imports
from django.contrib import admin

# Local Application Imports
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    '''
        Allows us to specify the order of fields in Admin
        NOTE : The first element of each tuple in fieldsets is the title of the fieldset
    '''
    fieldsets = [
        (None, {"fields" : ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
