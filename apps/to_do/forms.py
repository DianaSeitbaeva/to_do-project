from typing import (
    Type,
    Tuple,
)

from django import forms

from to_do.models import (
    Exercise,
)


class DateInput(forms.DateInput):  # noqa
    input_type = 'date'


class ExerciseCreationForm(forms.ModelForm):  # noqa
    class Meta:  # noqa
        model: Type[Exercise] = Exercise
        fields: Tuple[str] = (
            'finish_date_deadline', 'user',
            'description', 'activity',
        )
        widgets: dict = {
            'finish_date_deadline': DateInput(),
        }
