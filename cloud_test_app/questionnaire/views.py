from django.shortcuts import render
from .models import Questionnaire


def index(request):
    num_answers = Questionnaire.objects.all().count()
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)
