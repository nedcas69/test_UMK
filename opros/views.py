import random
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse

from opros.models import *


def index(request):
    pass
    question = Question.objects.all()
    answer = Answer.objects.all()
    keys = []
    dict_question = {}
    while range(10):
        key = random.randint(1,10)
        if Question.objects.get(id=key):
            if key not in keys:
                keys.append(key)
            else:
                continue
        else:
            continue

    for item in keys:
        dict_question = question.select_related('quiz').filter(id=item) + answer.select_related('question').filter(question_id=item)

    print(dict_question)
    
    return render(request, 'opros/index.html', {'questions': dict_question})