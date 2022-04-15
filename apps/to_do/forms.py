from django import forms

from .models import (
    Exercise,
)

class ExerciseCreationForm(forms.ModelForm):  # noqa

    class Meta:  # noqa
        model = Exercise
        fields = [
            'finish_date_deadline', 'user',
            'description', 'activity',
        ]
        