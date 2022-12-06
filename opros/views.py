import random
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from opros.forms import UserInputForm

from opros.models import *


def index(request, quiz_id, user_id):
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
    
    u_id = UserInput.objects.latest('id')
    user_id = u_id.id
    vars = {}
    result_i = 0
    for item in keys:
        if str(item) in request.POST:    
            if request.method == "POST":
                vars = request.POST[f'{item}']
                for item in ans:
                    if item.is_correct:
                        if vars == item.answer:
                            result_i += 1
                        else:
                            None    

                if result_i > 7:
                    user = UserInput.objects.filter(pk=user_id).update(result = True)
                else:
                    None
            else:
                None
        else:
            None


    print(vars)

    return render(request, 'opros/index.html', {'questions': questions, 'user_id': user_id})


def categories(request):
    quiz = Quiz.objects.all()
       
    return render(request, 'opros/categories.html', {'quiz': quiz})

def user_auth(request, quiz_id):
    u_i = UserInput.objects.latest('id')
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            question = Question.objects.all()
            user_input = form.save()
            return redirect(f'http://127.0.0.1:8000/questions/{quiz_id}/{u_i.id}/')
    else:
        form = UserInputForm()
    return render(request, 'opros/user_auth.html', {'form': form, 'quiz_id': quiz_id })

def results(request, id):
    user_input = UserInput.objects.filter(pk=id)
    for item in user_input:
        if item.is_correct:
            user_input = 'Вы прошли!!!'
        else:
            user_input = 'Вы не прошли.'

    return render(request, 'opros/results.html', {'user_input': user_input, 'id':id})
    
