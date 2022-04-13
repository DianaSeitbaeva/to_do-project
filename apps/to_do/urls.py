from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        '', 
        IndexView.as_view(),
        name='page_main'
    ),
    path(
        'show/<int:id>/',
        views.show,
        name='page_show'
    ),
] + static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
from django.urls import path

from to_do.views import (
    MainView,
    CreateExerciseView,
)

urlpatterns = [
    path('', MainView.as_view(), name="main_page"),
    path('add_exercise/', CreateExerciseView.as_view(), name="add_exercise")
]
