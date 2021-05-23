from dataclasses import dataclass, field
import datetime


@dataclass()
class Contact:
    id: int = field(init=False)
    name: str
    phone_number: str
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)
    deleted: bool = False

    def __repr__(self):
        return f"Entity: {self.__class__.__name__}<name: {self.name}>"

    def delete_user(self):
        self.deleted = True