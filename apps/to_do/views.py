
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from typing import Optional
from django.db.models import QuerySet
from to_do.models import Exercise


def create(request: WSGIRequest, ) -> HttpResponse:
    _form: HomeworkForm = HomeworkForm
    template_name: str = 'homework_create.html'

    todo: Exercise = _form.save(
            commit=False
        )
        todo.user = request.user
        todo.logo = request.FILES['logo']

        todo.save()

        context: dict = {
            'todo': todo
        }
        return self.get_http_response(
            request,
            'todo.html',
            context
        )

def show(request: WSGIRequest, description: str) -> HttpResponse:
    description: QuerySet = Exercise.objects.all(
        
    )
    context: dict = {
        'description': description
    }
    return render(
        request,
        template_name='todo.html',
        context=context,
    )

def register(request: WSGIRequest) -> HttpResponse:

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    if form.is_valid():
        user: CustomUser = form.save(
            commit = False
        )
        login: str = form.cleaned_data['login']
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_authenticate(
            email = email,
            password = password,
            login = login
        )
        if user and user.is_active:

            dj_login(request, user)

            return render(
                request,
                'brand/index.html'
            )
    context: dict = {
        'form': form
    }
    return render(
        request,
        'brand/register.html',
        context
    )


def login(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        email: str = request.POST['email']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            email = email,
            password = password
        )

        if not user:
            return render(
                request,
                'brand/login.html',
                {'error_message' : 'Неверные данные'}
            )
        if not user.is_active:
            return render(
                request,
                'brand/login.html',
                {'error_message' : 'Ваш аккаунт был удален'}
            )
        dj_login(request, user)

        return render(
            request,
            'brand/index.html'
        )
    return render(
        request,
        'brand/login.html'
    )


def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'form' : form,
    }
    return render(
        request,
        'brand/login.html',
        context
    )


class CreatePostView(ViewHandler,View):

    """Post Create View."""

    form: CreatedClothes = CreatedClothes
    template_name: str = 'brand/created.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        """GET request handler"""

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )
        if response:
            return response

        context: dict = {
            'form' : self.form
        }

        return self.get_http_response(
            request,
            self.template_name,
            context
        )

from typing import (
    Type,
    Any,
    Dict,
)

from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from to_do.models import Exercise
from to_do.forms import ExerciseCreationForm


class MainView(ListView):  # noqa
    model: Type[Exercise] = Exercise
    template_name: str = 'to_do/to_do.html'
    context_object_name: str = 'to_do_list'

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:  # noqa
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context['title'] = 'Страница заданий'
        return context


class CreateExerciseView(LoginRequiredMixin, CreateView):  # noqa
    raise_exception: bool = True
    form_class = ExerciseCreationForm
    template_name: str = 'to_do/created.html'
    success_url = reverse_lazy('main_page')
