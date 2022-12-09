import random
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from opros.forms import UserInputForm

from opros.models import *


keyz = []

def index(request, quiz_id):
    if request.method == 'POST':
        user_name = request.POST['user_name']

    i = 0
    questions = {}
    while i < 10:
        key = random.randint(1,Question.objects.filter(quiz_id = quiz_id).count())
        if Question.objects.filter(id=key, quiz_id = quiz_id):
            if key not in keyz:
                keyz.append(key)
                i += 1
            else:
                continue
        else:
            continue

    for item in keyz:
        ques = Question.objects.select_related('quiz').filter(id=item)
        ans = Answer.objects.select_related('question').filter(question_id=item)
        questions[ques] = ans
    
    return render(request, 'opros/index.html', {'questions': questions, 'user_name': user_name, 'quiz_id':quiz_id })

def categories(request):
    quiz = Quiz.objects.all()   
    return  render(request, 'opros/categories.html', {'quiz': quiz})

def user_auth(request, quiz_id):
    # u_i = UserInput.objects.latest('id')
    # u_i = u_i.id + 1
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            # question = Question.objects.all()
            user_input = form.save()
            # return redirect(f'http://127.0.0.1:8000/questions/{quiz_id}/{u_i}/')
    else:
        form = UserInputForm()
    return render(request, 'opros/user_auth.html', {'form': form, 'quiz_id': quiz_id })

def results(request, quiz_id):
    if request.method == "POST":
        user_name = request.POST['user_name']
        users = UserInput.objects.filter(user_name = user_name).last()
        user_id = users.id

    else:
        return redirect(f'http://127.0.0.1:8000/user_auth/{quiz_id}//')
      
    vars = {}
    is_correct = {}
    result_i = 0
    for item in keyz:   
            if request.method == "POST":
                vars[item] =  request.POST.get(f'{item}')
                is_correct[item] = Answer.objects.filter(question_id = item, is_correct = True)
            else:
                None        

    for key,value in vars.items(): 
        val = f'<QuerySet [<Answer: {value}>]>'
        is_corr = str(is_correct[key])
        if val == is_corr:
            result_i += 1

    if result_i > 7:
        UserInput.objects.filter(pk=user_id).update(result = True)
                    
    else:
        None

    print(result_i)

    user_input = UserInput.objects.filter(pk=user_id)
    template_name = 'opros/results.html'

    for item in user_input:
        if item.result:
            user_result = 'Вы прошли!!!'
        else:
            user_result = 'Вы не прошли.'

    keyz.clear()
    return render(request, 'opros/results.html', {'user_result': user_result,'user_input': user_input, 'user_id':user_id})
    
