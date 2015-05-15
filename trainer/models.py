from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

class TrainingDatum(models.Model):
	text = models.CharField(max_length=256, blank=True)
	categories = ArrayField(models.CharField(max_length=256, blank=True))