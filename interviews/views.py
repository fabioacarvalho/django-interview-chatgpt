from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404 as getor404, redirect

from jobs.models import Job
from interviews.models import *


def create_chat(request, job_id):
    if request.method == 'POST':
        job = getor404(Job, pk=job_id)
        chat = Chat.objects.create(job=job)
        return redirect('interviews:interview_chat', chat_uuid=chat.uuid)
    return HttpResponseNotAllowed(permitted_methods=['POST',])

def interview_chat(request, chat_uuid):

    chat = getor404(Chat, uuid=chat_uuid)
    chat_hidden = [1, 11, 12]
    return render(request, 'interviews/chat.html', locals())

def process_chat(request, chat_uuid):
    answer = request.POST.get('answer')
    if answer:
        chat = getor404(Chat, uuid=chat_uuid)
        Message.objects.create(
            chat=chat,
            role="user",
            content=answer,
        )

    return redirect('interviews:interview_chat', chat_uuid=chat_uuid)
