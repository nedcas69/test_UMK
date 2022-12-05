import random
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from opros.forms import UserInputForm

from opros.models import *


def index(request, quiz_id):
    keys = []
    i = 0
    questions = {}
    while i < 10:
        key = random.randint(1,13)
        if Question.objects.filter(id=key, quiz_id = quiz_id):
            if key not in keys:
                keys.append(key)
                i += 1
            else:
                continue
        else:
            continue

    for item in keys:
        ques = Question.objects.select_related('quiz').filter(id=item)
        ans = Answer.objects.select_related('question').filter(question_id=item)
        questions[ques] = ans

    print(keys)
    
    return render(request, 'opros/index.html', {'questions': questions})


def categories(request):
    quiz = Quiz.objects.all()
       
    return render(request, 'opros/categories.html', {'quiz': quiz})

def user_auth(request, quiz_id):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.save()
            return redirect(f'http://127.0.0.1:8000/questions/{quiz_id}')
    else:
        form = UserInputForm()
    return render(request, 'opros/user_auth.html', {'form': form, 'quiz_id': quiz_id})

def results(request):
    user_input = UserInput.objects.all()
    if request.method == 'POST':
        pass
    else:
        pass