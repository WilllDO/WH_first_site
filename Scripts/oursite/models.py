from django.conf import settings
from django.db import models
from django.utils import timezone


class Main(models.Model):
    def forUser(self):
        self.save()