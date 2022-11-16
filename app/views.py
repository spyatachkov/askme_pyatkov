from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Question, Answer, Tag, Profile

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
    context['questions'] = paginate(Question.objects.new(), request)
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    try:
        context['question'] = Question.objects.get(pk=question_id)
        context['answers'] = Answer.objects.hot(question_id)
        return render(request, 'question.html', context=context)
    except:
        return render(request, '404.html', context=context)


def signup(request):
    return render(request, 'signup.html', context=context)


def login(request):
    return render(request, 'login.html', context=context)


def settings(request):
    return render(request, 'settings.html', context=context)


def ask(request):
    return render(request, 'ask.html', context=context)


def hot(request):
    context['questions'] = paginate(Question.objects.hot(), request)
    return render(request, 'hot_questions.html', context=context)


def tag(request, tag_name):
    try:
        context['questions'] = paginate(Question.objects.get_by_tag(tag_name), request)
        context['tag_name'] = tag_name
        return render(request, 'questions_list.html', context=context)

    except:
        return render(request, '404.html', context=context)


context = {
        'popular_tags': Tag.objects.popular(),
        'best_members': Profile.objects.best(),
        'is_auth': authFlag
}
