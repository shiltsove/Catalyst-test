from django.contrib import admin
from django.urls import path

from questionnaire import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    # path('results/', views.results, name='results'),


]
