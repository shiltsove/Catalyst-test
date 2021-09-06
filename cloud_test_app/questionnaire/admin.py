from django.contrib import admin
from questionnaire.models import Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('month', 'day')

    list_filter = ('month', 'day')


admin.site.register(Questionnaire, QuestionnaireAdmin)
