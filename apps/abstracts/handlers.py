from lib2to3.pgen2.token import OP
from re import template
from typing import Optional

from urllib import response
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from abstracts.mixins import HttpResponseMixin

class ViewHandler(HttpResponseMixin):
    """Handler for vlidating request and generating response"""

    def get_validated_response(
        self,
        request: WSGIRequest
    ) -> Optional[HttpResponse]:
        """GET validated response"""

        return self.get_http_response(
            request
        )

        response: Optional[HttpResponse] = \
            self.get_validated_response(
                request
            )

        if response:
            return response