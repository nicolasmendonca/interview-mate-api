from rest_framework import viewsets
from .models import CatalogQuestion
from .serializers import CatalogQuestionSerializer

class CatalogQuestionViewSet(viewsets.ModelViewSet):
  serializer_class = CatalogQuestionSerializer
  queryset = CatalogQuestion.objects.all()

