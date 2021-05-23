from contacts.domain.models.contact import Contact
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ListContacts(models.Model):
    user_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(Contact)

    class Meta:
        ordering = ['id']
        verbose_name = 'List Contact'
        verbose_name_plural = "List Contacts"

    def __str__(self):
        return self.id