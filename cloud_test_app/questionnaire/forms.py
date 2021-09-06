from django.forms import ModelForm
from .models import Questionnaire


class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Questionnaire
        fields = [
            'month',
            'day',
        ]

        labels = {
            'month': 'My favorite month',
            'day': 'My favorite day of the week',
        }
