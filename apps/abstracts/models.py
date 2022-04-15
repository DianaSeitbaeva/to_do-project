from django.db import models


class AbstractDateTime(models.Model):  # noqa
    date_time_created = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )
    date_time_deleted = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        blank=True,
        auto_now=True
    )
    date_time_live = models.DateTimeField(
        verbose_name='Время существования',
        null=True,
        blank=True,
    )

    class Meta:  # noqa
        abstract = True
