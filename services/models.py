from django.db import models
from simple_history.models import HistoricalRecords


class Service(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    category = models.ForeignKey('Category', on_delete = models.PROTECT, null = True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 50, db_index = True)

    def __str__(self):
        return self.name