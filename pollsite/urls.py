'''
    Purpose : URL configuration for pollsite project, where we include the url configurations of various apps in the project
    Author : Rohit Pai
    Date : 10th July 2024
'''

# Standard Library Imports

# Third Party Imports
from django.contrib import admin
from django.urls import include, path

# Local Application Imports


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
