import random
import re
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from opros.forms import UserInputForm

from opros.models import *




def index(request, quiz_slug):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        form = UserInputForm(request.POST)
        if form.is_valid():
            # question = Question.objects.all()
            user_input = form.save()
    else:
        return redirect(f'http://127.0.0.1:8000/user_auth/{quiz_slug}/')
    keyz = []
    i = 0
    questions = {}
    quiz = Quiz.objects.filter(slug=quiz_slug).last()
    quizid = quiz.id
    ques_first = Question.objects.filter(quiz_id=quizid).first()
    ques_first = int(ques_first.id)
    ques_last = Question.objects.filter(quiz_id=quizid).last()
    ques_last = int(ques_last.id)

    while i < 10:
        key = random.randint(ques_first, ques_last)
        if Question.objects.filter(id=key, quiz_id = quizid):
            if key not in keyz:
                keyz.append(key)
                i += 1
            else:
                continue
        else:
            continue

    if request.method == "POST":
        user_name = request.POST['user_name']
        users = UserInput.objects.filter(user_name = user_name).last()
        user_id = users.id
        UserInput.objects.filter(pk=user_id).update(random_list = keyz)


    for item in keyz:
        ques = Question.objects.select_related('quiz').filter(id=item)
        ans = Answer.objects.select_related('question').filter(question_id=item)
        questions[ques] = ans
    print(keyz)
    return render(request, 'opros/index.html', {'questions': questions, 'user_name': user_name, 'quiz_slug': quiz_slug })

def categories(request):
    quiz = Quiz.objects.all()   
    return  render(request, 'opros/categories.html', {'quiz': quiz})

def user_auth(request, quiz_slug):
    # u_i = UserInput.objects.latest('id')
    # u_i = u_i.id + 1
    if request.method == 'POST':
        form = UserInputForm(request.POST)
    else:
        form = UserInputForm()
    return render(request, 'opros/user_auth.html', {'form': form, 'quiz_slug': quiz_slug })

def results(request, quiz_slug):
    
    if request.method == "POST":
        user_name = request.POST['user_name']
        users = UserInput.objects.filter(user_name = user_name).last()
        user_id = users.id
    else:
        return redirect(f'http://127.0.0.1:8000/user_auth/{quiz_slug}//')
    rand_list = (users.random_list)  
    rand_list = str(rand_list)
    vars = {}
    questions_results = []
    is_correct = {}
    result_i = 0
    keyz = []
    for item in rand_list.split():
        x = re.findall(r'\d+', item)
        for item in x:
            keyz.append(item)
            

    for item in keyz:   
            if request.method == "POST":
                vars[item] =  request.POST.get(f'{item}')
                is_correct[item] = Answer.objects.filter(question_id = item, is_correct = True)       

    for key,value in vars.items(): 
        val = f'<QuerySet [<Answer: {value}>]>'
        is_corr = str(is_correct[key])
        if val == is_corr:
            result_i += 1
            good = str(value) + '  +++'
            questions_results.append(good)

        else:
            bad = str(value) + '  X'
            questions_results.append(bad)



    if result_i > 7:
        UserInput.objects.filter(pk=user_id).update(result = True)
                    
    else:
        UserInput.objects.filter(pk=user_id).update(result = False)

    print(result_i)
    print(keyz)

    user_input = UserInput.objects.filter(pk=user_id)
    template_name = 'opros/results.html'

    for item in user_input:
        if item.result:
            user_result = 'Вы прошли!!!'
        else:
            user_result = 'Вы не прошли.'
    keyz.clear()
    return render(request, 'opros/results.html', {'user_result': user_result,'user_input': user_input, 'user_id':user_id, 'result_i': result_i, 'questions_results': questions_results})
    
