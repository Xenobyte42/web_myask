from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import *
from .forms import *


popular_tags = ['Pigs', 'Evangelion', 'Cats',
                'ManBearPig', '42', 'Pony']

best_members = ['Kurt Cobain', 'Eyes Adrift', 'Blink-182',
                'AC↯DC', '♪Metallica♪']

user = Profile.objects.all()[0]

def paginate(objects, request, amount):
    paginator = Paginator(objects, amount)
    page = request.GET.get('page')
    return paginator.get_page(page)

def hot_page(request):
    question_list = Question.objects.top()
    
    visible_questions = paginate(question_list, request, 4)
    return render(request, 'hot.html', {'questions': visible_questions,
                                        'popular_tags': popular_tags,
                                        'best_members': best_members,
                                        'user': user})

def main_page(request):
    question_list = Question.objects.get_list()
    visible_questions = paginate(question_list, request, 4)
    return render(request, 'index.html', {'questions': visible_questions,
                                        'popular_tags': popular_tags,
                                        'best_members': best_members,
                                        'user': user})

def tag_page(request, tag_name):
    question_list = Question.objects.get_tag(tag_name)

    visible_questions = paginate(question_list, request, 4)
    return render(request, 'tag.html', {'tag_name': tag_name,
                                        'questions': visible_questions,
                                        'popular_tags': popular_tags,
                                        'best_members': best_members,
                                        'user': user})

def question_page(request, question_id):
    main_question = Question.objects.get_question(question_id)
    answers = Answer.objects.answer(question_id)
        
    return render(request, 'question.html', {'main_question': main_question,
                                             'answers': answers,
                                             'popular_tags': popular_tags,
                                             'best_members': best_members,
                                             'user': user})

def login_page(request):
    return render(request, 'login.html', {'popular_tags': popular_tags,
                                          'best_members': best_members})

def signup_page(request):
    return render(request, 'signup.html', {'popular_tags': popular_tags,
                                           'best_members': best_members})

def ask_page(request):
    return render(request, 'ask.html', {'popular_tags': popular_tags,
                                        'best_members': best_members,
                                        'form': QuestionForm()})

def settings_page(request):
    return render(request, 'settings.html', {'popular_tags': popular_tags,
                                             'best_members': best_members})


