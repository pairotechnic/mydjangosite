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
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Local Application Imports
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Return the last 5 published questions 
        # ( not including those set to be published in the future )
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model=Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model=Question
    template_name = "polls/results.html"

def vote(request, question_id):
    '''
        Updates the count of selected choice for the given question if it exists
    '''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render (
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else : 
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if the user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))

