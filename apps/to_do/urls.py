from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path
)
from to_do.views import (
    CreateToDoView,
    ExerciseApiView
)


urlpatterns = [

    path(
        '', 
        ExerciseApiView.as_view(),
        name='page_main'
    )
] + static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)





