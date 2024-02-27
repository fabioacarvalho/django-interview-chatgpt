from django.shortcuts import render

from jobs.models import Job


def list_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/list.html', {"page_title": "Lista de Vagas", "jobs": jobs})
