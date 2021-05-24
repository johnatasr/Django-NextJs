from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_201_CREATED,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import viewsets

from contacts.presenters.factory import ContactsFactory
from contacts.presenters.helpers import clear_cache
from configs.exceptions import ContactsException

from django.core.cache import cache

# Register your viewsets here.
class ContactsViewSet(viewsets.GenericViewSet):
    """
    API made using Django Rest Framework
    """

    factory = ContactsFactory()
    http_method_names = ["get", "post", "put", "delete"]

    @action(methods=["GET"], detail=False, url_path="contacts/(?P<id>[0-9]+)/search")
    @method_decorator(cache_page(30 * 2))
    def get(self, request, id=None) -> Response:
        """
           Endpoint to search a list of contacts or a specific contact by id
           :param request:
           :param id: int
           :return: dict
        """
        try:
            results = self.factory.create_get_iterator(user_id=request.user.id, id_params=id if id else None)
            return Response(results, status=HTTP_200_OK)
        except Exception as error:
            if isinstance(error, ContactsException):
                return Response({"msg": error.args[0]}, status=HTTP_200_OK)
            else:
                return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["POST"], detail=False, url_path="contacts")
    @clear_cache
    def post(self, request) -> Response:
        """
           Endpoint to record a contact by method POST
           :param request:
           :return: dict
        """
        try:
            cache.clear()
            results = self.factory.create_post_iterator(data=request.data, user_id=request.user.id)
            return Response(results, status=HTTP_201_CREATED)
        except Exception as error:
            if isinstance(error, ContactsException):
                return Response({"msg": error.args[0]}, status=HTTP_200_OK)
            else:
                return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["PUT"], detail=False, url_path="contacts/(?P<id>[0-9]+)/update")
    @clear_cache
    def put(self, request, id: int) -> Response:
        """
           Endpoint to update a contact by passed id in params
           :param request:
           :return: dict
        """
        try:
            cache.clear()
            results = self.factory.create_update_iterator(data=request.data, contact_id=id)
            return Response(results, status=HTTP_200_OK)
        except Exception as error:
            if isinstance(error, ContactsException):
                return Response({"msg": error.args[0]}, status=HTTP_200_OK)
            else:
                return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["DELETE"], detail=False, url_path="contacts/(?P<id>[0-9]+)/delete")
    @clear_cache
    def delete(self, request, id) -> Response:
        """
           Endpoint to delete a contact by passed id in params
           :param request:
           :return: dict
        """
        try:
            cache.clear()
            results = self.factory.create_delete_iterator(contact_id=id)
            return Response(results, status=HTTP_200_OK)
        except Exception as error:
            if isinstance(error, ContactsException):
                return Response({"msg": error.args[0]}, status=HTTP_200_OK)
            else:
                return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)