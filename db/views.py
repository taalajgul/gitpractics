from django.db import models
from django.shortcuts import render, request
from .models import Person
 from django.views import View


class PersonView(View):
    def get(self, request): 
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'persons.html', context) 