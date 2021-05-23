from contacts.domain.use_cases.create_contact import CreateContactCase
from configs.exceptions import IteratorException


class CreateContactIterator(CreateContactCase):
    """
    Iteractor responsible for create a contact, called by API
    """
    def __init__(self, validator=None, repo=None, serializer=None, entity=None):
        self.validator: object = validator
        self.repo: object = repo()
        self.serializer: object = serializer
        self.contact_entity: object = entity

    def set_params(self, contact_payload: dict, user_id: int):
        self.contact_payload = contact_payload
        self.user_id = user_id
        return self

    def execute(self):
        try:
            valided_payload: bool = self.validator().validate_payload(self.contact_payload)

            if valided_payload:
                created_user = self.create_by_payload()

                serialized_user: dict = self.serializer(
                    contact=created_user, msg="Contact created"
                ).create_message()
                return serialized_user
        except IteratorException as error:
            raise IteratorException(error)

    def create_by_payload(self) -> object:
        try:
            return self.repo.create_contact(
                contact=self.contact_entity(
                    name=self.contact_payload['name'],
                    phone_number=self.contact_payload['phoneNumber']
                ),
                user_id=self.user_id
            )
        except IteratorException as error:
            raise IteratorException(error)

