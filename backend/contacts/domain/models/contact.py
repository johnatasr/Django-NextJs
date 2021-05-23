from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=144, null=True, blank=True)
    phone_number = models.CharField(max_length=144, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name