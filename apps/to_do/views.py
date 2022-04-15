from typing import Optional
from urllib import response
from .serializer import ExerciseSerializer

from rest_framework import generics
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import QuerySet
from django.views import View


from abstracts.mixins import HttpResponseMixin
from abstracts.handlers import ViewHandler
from to_do.forms import ExerciseCreationForm
from .models import Exercise


class ExerciseApiView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class CreateToDoView(ViewHandler,View):

    """Create To do View"""

    
    form: ExerciseCreationForm = ExerciseCreationForm
    template_name: str = 'to_do/created.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler"""

        context: dict = {
            'form' : self.form
        }

        return self.get_http_response(
            request,
            self.template_name,
            context
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """POST request handler"""

        form: ExerciseCreationForm = self.form(
            request.POST
        )

        if not form.is_valid():
            context: dict = {
                'form' : form
            }
            return self.get_http_response(
                request,
                self.template_name,
                context
            )

        exrecise : Exercise = form.save(
            commit=False
        )
        exercise.save()

        context: dict = {
            'exercise' : exercise
        }

        template_name : str = 'to_do/main.html'
        return self.get_http_response(
            request,
            template_name,
            context
        )



