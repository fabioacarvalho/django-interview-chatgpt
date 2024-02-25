from django.db import models
import uuid
from .choices import *
from django.conf import settings

from .services import GptService

class Chat(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=300, verbose_name='Title')
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, verbose_name='Job')
    completed = models.BooleanField(default=False, verbose_name='Completed')

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
            self.title = f'Chat {self.job.title} - {self.uuid}'
            super().save(*args, **kwargs)
            initial_prompt = settings.INITIAL_PROMPT_TEMPLATE
            initial_prompt = initial_prompt.replace("{job_title}", self.job.title)
            initial_prompt = initial_prompt.replace("{job_requirements}", self.job.requirements)
            initial_prompt = initial_prompt.replace("{job_responsibilities}", self.job.responsibilities)
            Message.objects.create(chat=self, role="system", content=initial_prompt)
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey('interviews.Chat', on_delete=models.CASCADE, verbose_name='Chat')
    role = models.CharField(max_length=9, choices=ROLE_CHOICES, verbose_name='Role')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def save(self, *args, **kwargs):
        if not self.pk and self.role != 'assistant' and not self.chat.completed:
            super().save(*args, **kwargs)

            if self.role == 'user' and self.chat.message_set.filter(role="assistant").count() >= 5:
                Message.objects.create(
                    chat=self.chat,
                    role="system",
                    content="Realize o feedback do candidato, esse feedback deve informar quais foram os pontos positivos, os pontos negativos, o que pode ser melhorado e se o candidato possui um perfil adquado para a vaga."
                )

                self.chat.completed = True
                self.chat.save()
            else:
                service = GptService()
                Message.objects.create(
                    chat=self.chat,
                    role="assistant",
                    content=service.get_chat_completion(self.chat.message_set.all())
                )
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.role} - {self.chat.title}'
