from django.db.models import Count

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from locking.models import NonBlockingLock

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
            lock = NonBlockingLock.objects.acquire_lock(
                    lock_name="saving_questionnaire"
                )
            question_form.save()
            lock.release()
            return HttpResponseRedirect(
                reverse(
                    'questionnaire'
                ))

    context = {
        "title": "Fill questionnaire!",
        'question_form': question_form,
    }
    return render(request, "questionnaire/questionnaire.html", context)


def results(request):
    question_list = Questionnaire.objects.all()
    answers_total = question_list.count()
    human_readable_days = dict(Questionnaire.DAY_CHOICES)
    human_readable_months = dict(Questionnaire.MONTH_CHOICES)

    def form_and_replenish_readable_statistic(objects, fieldname, dicionary):
        field_count = objects.values(fieldname).annotate(the_count=Count(fieldname))
        for field in field_count:
            field[fieldname] = dicionary[field[fieldname]]
            field["percent"] = round(100 * float(field["the_count"])/float(answers_total), 1)
        return field_count

    month_fav_day = []
    months_in_questionnare = question_list.values_list('month', flat=True).distinct()

    for month in months_in_questionnare:
        fav_day = question_list\
            .filter(month=month)\
            .values('day')\
            .annotate(the_count=Count('day'))\
            .order_by('-the_count')\
            .first()['day']
        month_fav_day.append({
            'month': human_readable_months[month],
            'day': human_readable_days[fav_day]
        })

    context = {
        "title": "Results",
        "question_list": question_list,
        "days_statistic": form_and_replenish_readable_statistic(question_list, "day", human_readable_days),
        "months_statistic": form_and_replenish_readable_statistic(question_list, "month", human_readable_months),
        "month_fav_day": month_fav_day
    }
    return render(request, "questionnaire/results.html", context)
