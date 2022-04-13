from django.contrib import admin
from django.template.defaultfilters import truncatechars

from to_do.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):  # noqa
    readonly_fields: tuple = (
        'date_time_created', 'date_time_deleted',
        'existance_duration',
    )
    list_display: tuple = (
        'id', 'user', 'short_description',
        'finish_date_deadline', 'activity',
    )
    list_display_links: tuple = (
        'id', 'short_description',
    )
    list_editable: tuple = (
        'activity',
    )
    search_fields: tuple = (
        'description',
    )
    list_filter: tuple = (
        'activity',
    )
    save_on_top: bool = True

    def short_description(self, obj) -> str:  # noqa
        DESCRIPTION_MAX_LENGTH = 40
        return truncatechars(obj.description, DESCRIPTION_MAX_LENGTH)
    short_description.short_description = 'Описание'
