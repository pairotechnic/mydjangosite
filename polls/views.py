'''
    Purpose : Collection of different views that will be displayed on the screen
    Author : Rohit Pai
    Date : 10th July 2024

    NOTE : 
    These are the most basic views possible in Django. 
    Refer to urls.py, for information on how to access/display this view
'''

# Standard Library Imports

# Third Party Imports
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Local Application Imports
from .models import Question

def index(request):
    '''
        Gets the latest 5 questions by publication date and passes it to a template
    '''
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    context = {
        "latest_question_list" : latest_question_list
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(requests, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request_id, question_id):
    return HttpResponse("You're voting on question %s." % question_id)