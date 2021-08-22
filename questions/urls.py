from rest_framework import routers
from .views import CatalogQuestionViewSet

router = routers.SimpleRouter()
router.register(r'catalog_questions', CatalogQuestionViewSet, basename='catalog-questions')
