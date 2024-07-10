'''
    Purpose : Displays a Hello World message on the screen
    Author : Rohit Pai
    Date : 10th July 2024

    NOTE : 
    This is the most basic view possible in Django. 
    Refer to urls.py, for information on how to access/display this view
'''

# Standard Library Imports

# Third Party Imports
from django.http import HttpResponse

# Local Application Imports

def index(request):
    '''
        Displays a Hello World message on the screen
    '''
    return HttpResponse("Hello World. You're at the polls index.")