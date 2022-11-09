from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import models

authFlag = True


def paginate(object_list, request):
    paginator = Paginator(list(object_list), 10)
    p = request.GET.get('page')
    try:
        page = paginator.get_page(p)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def index(request):
    context = {'questions': paginate(models.QUESTIONS, request), 'is_auth': authFlag}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    context = {'is_auth': authFlag}
    try:
        question_item = models.QUESTIONS[question_id]
        context = {'question': question_item, 'is_auth': authFlag}
        return render(request, 'question.html', context=context)

    except:
        return render(request, '404.html', context=context)


def signup(request):
    context = {'is_auth': authFlag}
    return render(request, 'signup.html', context=context)


def login(request):
    context = {'is_auth': authFlag}
    return render(request, 'login.html', context=context)


def settings(request):
    context = {'is_auth': authFlag}
    return render(request, 'settings.html', context=context)


def ask(request):
    context = {'is_auth': authFlag}
    return render(request, 'ask.html', context=context)


def hot(request):
    context = {'questions': paginate(models.HOT_QUESTIONS, request), 'is_auth': authFlag}
    return render(request, 'hot_questions.html', context=context)


def tag(request, tag_name):
    context = {'is_auth': authFlag}
    try:
        context = {'questions': paginate(models.QUESTIONS, request), 'is_auth': authFlag, 'tag_name': tag_name}
        return render(request, 'questions_list.html', context=context)

    except:
        return render(request, '404.html', context=context)
