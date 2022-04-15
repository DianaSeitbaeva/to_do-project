from datetime import (
    date,
)

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from abstracts.models import AbstractDateTime




class Exercise(AbstractDateTime):  

    finish_date_deadline = models.DateField(
        verbose_name='Заданное время выполнения',
    )

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )

    activity = models.BooleanField(
        verbose_name='Активность',
        default=True
    )

    def __str__(self) -> str:  
        return f'Домашка пользователя {self.user.username}'

    class Meta:  
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['id', ]

    
