class ContactsException(Exception):
    """
        Exception base
    """
    def __init__(self, source, code, message):
        super().__init__(message)
        self._source = source
        self._code = code

    @property
    def source(self):
        return self._source

    @property
    def code(self):
        return self._code


class InvalidPayloadException(ContactsException):
    """
       Exception to Validators
    """
    pass


class ConflictException(ContactsException):
    """
        Exception to general conflits
    """
    pass


class IteratorException(ContactsException):
    """
        Exception to Iterators
    """
    def __init__(self, process):
        super().__init__(source='interator', code='error', message=f"Erro em : {process}")


class EntityException(ContactsException):
    """
        Exception to Entities
    """
    pass


class EntityDoesNotExistException(ContactsException):
    """
        Exception to Entities if doesn't exists
    """

    def __init__(self, entity):
        super().__init__(source='entity', code='not_found', message=f'Entidade: {entity} não encotrada ')