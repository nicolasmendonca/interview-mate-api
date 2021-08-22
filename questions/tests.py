from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from questions.models import CatalogQuestion


class CatalogQuestionCreateTest(APITestCase):
  def test_create_catalog_question_success(self):
    url = reverse('catalog-questions-list')
    data = {
        "question": "Compare `useState` vs `useReducer`",
        "help_text": "`useState` is an implementation of `useReducer`",
        "description": "`useState` is an implementation of `useReducer`",
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(CatalogQuestion.objects.count(), 1)
    self.assertEqual(CatalogQuestion.objects.get().question, data['question'])

  def test_create_catalog_question_error(self):
    url = reverse('catalog-questions-list')
    data = {
        "question": "Compare `useState` vs `useReducer`" * 2000,
        "help_text": "`useState` is an implementation of `useReducer`" * 2000,
        "description": "`useState` is an implementation of `useReducer`" * 2000,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CatalogQuestionListTest(APITestCase):
  def setUp(self):
    self.saved_question = CatalogQuestion.objects.create(
      question="Some question",
      help_text="Help text",
      description="Description",
    )

  def test_list_catalog_questions(self):
    url = reverse('catalog-questions-list')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['question'], self.saved_question.question)
    self.assertEqual(response.data[0]['help_text'], self.saved_question.help_text)
    self.assertEqual(response.data[0]['description'], self.saved_question.description)

