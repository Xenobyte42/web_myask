from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage
from django.views import View
from .models import *
from .forms import *

from mysite import settings

popular_tags = ['Pigs', 'Evangelion', 'Cats',
                'ManBearPig', '42', 'Pony']

best_members = ['Kurt Cobain', 'Eyes Adrift', 'Blink-182',
                'AC↯DC', '♪Metallica♪']

def paginate(objects, request, amount):
    paginator = Paginator(objects, amount)
    page = request.GET.get('page')
    return paginator.get_page(page)


class MainPage(View):
    template_name = 'index.html'

    def get(self, request):
        question_list = Question.objects.get_list()
        visible_questions = paginate(question_list, request, settings.QUEST_PER_PAGE)
        context = {'questions': visible_questions, 'popular_tags': popular_tags,
                   'best_members': best_members, 'user': request.user}
        return render(request, self.template_name, context)


class HotPage(View):
    template_name = 'hot.html'

    def get(self, request):
        question_list = Question.objects.top()
        visible_questions = paginate(question_list, request, settings.QUEST_PER_PAGE)
        context = {'questions': visible_questions, 'popular_tags': popular_tags,
                   'best_members': best_members, 'user': request.user}
        return render(request, self.template_name, context)


class TagPage(View):
    template_name = 'tag.html'

    def get(self, request, tag_name):
        question_list = Question.objects.get_tag(tag_name)
        visible_questions = paginate(question_list, request, settings.QUEST_PER_PAGE)
        context = {'questions': visible_questions, 'popular_tags': popular_tags,
                   'best_members': best_members, 'user': request.user, 'tag_name': tag_name}
        return render(request, self.template_name, context)


class QuestionPage(View):
    template_name = 'question.html'

    def get(self, request, question_id):
        main_question = Question.objects.get_question(question_id)
        answers = Answer.objects.answer(question_id)
        context = {'main_question': main_question, 'answers': answers,
                   'popular_tags': popular_tags, 'best_members': best_members,
                   'user': request.user}
        return render(request, self.template_name, context)


class SignupPage(View):
    template_name = 'signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        context = {'popular_tags': popular_tags,
                   'best_members': best_members,
                   'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(user.password)
            user.save()
            return redirect('login')
        context = {'popular_tags': popular_tags,
                   'best_members': best_members,
                   'form': form}
        return render(request, self.template_name, context)


class AskPage(View):
    template_name = 'ask.html'
    form_class = AskForm

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class()
        context = {'popular_tags': popular_tags,
                   'best_members': best_members,
                   'form': form}
        return render(request, self.template_name, context)


class SettingsPage(View):
    template_name = 'settings.html'
    form_class = SettingsForm

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class(instance=request.user)
        context = {'popular_tags': popular_tags,
                   'best_members': best_members,
                   'form': form}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid:
            user = form.save(commit=False)
            user.save()
        context = {'popular_tags': popular_tags,
                   'best_members': best_members,
                   'form': form}
        return render(request, self.template_name, context)

