from django.db import models

class CatalogQuestion(models.Model):
  ANSWER_TYPES = (
        ('percentage', 'Percentage'),
    )
  question = models.CharField(max_length=2000)
  help_text = models.CharField(max_length=2000, blank=True)
  description = models.CharField(max_length=2000, blank=True)
  type = models.CharField(choices=ANSWER_TYPES, default="percentage", max_length=255)
