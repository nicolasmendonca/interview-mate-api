from rest_framework import serializers
from .models import CatalogQuestion

class CatalogQuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = CatalogQuestion
    fields = ['id', 'question', 'help_text', 'description', 'type']
