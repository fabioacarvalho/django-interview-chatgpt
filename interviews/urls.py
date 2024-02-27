
from django.urls import path
from interviews.views import *


app_name = 'interviews'
urlpatterns = [
    path('create/<int:job_id>', create_chat, name='create_chat'),
    path('chat/<str:chat_uuid>', interview_chat, name='interview_chat'),
    path('answer/<str:chat_uuid>', process_chat, name='process_chat'),
]
