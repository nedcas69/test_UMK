import random
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from opros.forms import UserInputForm

from opros.models import *


def index(request, quiz_id):
    keys = []
    answs = []

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
        j = 0
        while j < 4:
            an = Answer.objects.latest('id')
            answ = random.randint(1,an.id)
            qwe = Answer.objects.get(id=answ)
            rty = Answer.objects.filter(question_id=item)
            if Answer.objects.filter(id__in=[answ], question_id=item):
                if answ not in answs:
                    answs.append(answ)
                    j += 1
                else:
                    continue
            else:
                continue
        for answ_item in answs:
            ans = Answer.objects.select_related('question').filter(pk=answ_item)
            answers = ans 


        questions[ques] = answers

    print(questions)
    print(answs)
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