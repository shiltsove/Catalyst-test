from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import QuestionForm
from .models import Questionnaire


def index(request):
    num_answers = Questionnaire.objects.all().count()
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)


def questionnaire(request):
    question_form = QuestionForm()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return HttpResponseRedirect(
                reverse(
                    'questionnaire'
                ))

    context = {
        "title": "Fill questionnaire!",
        'question_form': question_form,
    }
    return render(request, "questionnaire/questionnaire.html", context)
