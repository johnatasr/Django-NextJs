from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from .interfaces import ISerializer


class ContactSerializer(ISerializer):
    def __init__(self, contact: object, msg: str = None):
        self.contact = contact
        self.msg = msg

    def mount_payload(self) -> dict:
        payload: dict = {
            "msg": self.msg if self.msg else "",
            "contact": {
                "id": self.contact.id,
                "name": self.contact.name,
                "phoneNumber": self.contact.phone_number,
            }
        }
        return payload

    def create_message(self) -> dict:
        message = self.mount_payload()
        return message


class ListContactsSerializer(ISerializer):
    def __init__(self, list_contacts: object):
        self.list_contacts = list_contacts

    def mount_list_contacts(self) -> list:
        list_contc: list = []
        for usr in self.list_contacts.contacts:
            contact: dict = {
                "id": usr.id,
                "name": usr.name,
                "phoneNumber": usr.phone_number,
            }
            list_contc.append(contact)
        return list_contc

    def mount_payload(self) -> dict:
        contacts: dict = self.mount_list_contacts()

        return {
            "contacts": contacts,
            "contactsCount": len(contacts)
        }

    def create_message(self) -> dict:
        message: dict = self.mount_payload()
        return message


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['id'] = user.id

        return token


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance