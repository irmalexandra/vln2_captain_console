from django.db import models

from consoles.models import Consoles


class Games(models.Model):
    console = models.ForeignKey(Consoles)


