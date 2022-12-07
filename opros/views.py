import random
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from opros.forms import UserInputForm

from opros.models import *

keyz = []
print(keyz)
def index(request, quiz_id, user_id):
    
    i = 0
    questions = {}
    while i < 10:
        key = random.randint(1,13)
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

    
    
    
    u_id = UserInput.objects.latest('id')
    user_id = u_id.id
    # vars = {}
    # result_i = 0
    # for item in keys:
    #     # if str(item) in request.POST:    
    #         if request.method == "POST":
    #             vars[item] =  request.POST.get(f'{item}')
                
    #             # for item in ans:
    #             #     if item.is_correct:
    #             #         if vars == item.answer:
    #             #             result_i += 1
    #             #         else:
    #             #             None    

                
    #         else:
    #             None
    #     # else:
    #     #     None
    # for key,value in vars.items(): 
    #     if value == 'True':
    #         print(value)
    #         result_i += 1

    # print(result_i)
    # if result_i > 7:
    #     UserInput.objects.filter(pk=user_id).update(result = True)
                    
    # else:
    #     None

    # print(vars)
    # form = UserResultForm(request.POST)
    return render(request, 'opros/index.html', {'questions': questions, 'user_id': user_id, 'keyz':keyz})

def categories(request):
    quiz = Quiz.objects.all()
       
    return  render(request, 'opros/categories.html', {'quiz': quiz})

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

def results(request,user_id):
    u_id = UserInput.objects.latest('id')
    user_id = u_id.id
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
        if value == 'True':
            print(value)
            result_i += 1

    print(result_i)
    if result_i > 7:
        UserInput.objects.filter(pk=user_id).update(result = True)
                    
    else:
        None

    print(vars)


    user_input = UserInput.objects.filter(pk=user_id)
    template_name = 'opros/results.html'
    for item in user_input:
        if item.result:
            user_input = 'Вы прошли!!!'
        else:
            user_input = 'Вы не прошли.'
    keyz.clear()
    return render(request, 'opros/results.html', {'user_input': user_input, 'user_id':user_id})
    
