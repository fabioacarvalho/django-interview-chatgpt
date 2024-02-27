from django.db import models
from .choices import *


class Job(models.Model):
    title = models.CharField(max_length=300, verbose_name='Job')
    description = models.TextField(verbose_name='Description')
    requirements = models.TextField(verbose_name='Requirements')
    responsibilities = models.TextField(verbose_name='Responsibilities')
    level = models.CharField(max_length=20, verbose_name='Level', choices=LEVEL_CHOICES)
    skills = models.ManyToManyField("jobs.Skill", verbose_name='Skill')


    def requirements_list(self):
        return self.requirements.split("\n")

    def responsibilities_list(self):
        return self.responsibilities.split("\n")

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=300, verbose_name='Skill')

    def __str__(self):
        return self.title
