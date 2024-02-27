from django.urls import path
from jobs.views import *


app_name = 'jobs'
urlpatterns = [
    path('', list_jobs, name='list')
]
