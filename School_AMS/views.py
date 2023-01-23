from django.shortcuts import render
from .models import Student, Faculty, Finance


def index(request):
    return render( request, 'School_AMS/index.html', {
    'students': Student.objects.all()
    })


