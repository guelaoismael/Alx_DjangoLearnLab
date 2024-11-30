from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class BookApiTestCase(APITestCase):
  def setUp(self):
   
   self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
   self.login_url = reverse('login')
   
   self.book1 = Book.objects.create(
      title = "Book 1",
      author = "Anonymous", 
      publication_year=2023
    )

   self.book2 = Book.objects.create(
      title = "Book 2",
      author = "Anonymous writer", 
      publication_year=2022
    )
   self.url = reverse('book-list')


  def test_authenticated_access(self):
    # Log in the test user
    login_successful = self.client.login(username='testuser', password='testpassword')
    self.assertTrue(login_successful)

    # Make an authenticated request
    response = self.client.get(reverse('some_authenticated_view'))
    self.assertEqual(response.status_code, 200)
    
  def test_create_book(self):
      # create_url = reverse('book-create')
      data = {
        'title':'New Book',
        'author': 'New author',
        'publication_year': 2021
      }
      response = self.client.post(self.url, data, format='json')

      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      
      self.assertEqual(Book.objects.count(), 3)
  def test_retrieve_books(self):
      
      response = self.client.get(self.url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 2)

  def test_update_book(self):
      # Test updating a book
      update_url = reverse('book-detail', args=[self.book1.id])
      data = {"title": "Updated Book 1"}
      response = self.client.patch(update_url, data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.book1.refresh_from_db()
      self.assertEqual(self.book1.title, "Updated Book 1")

  def test_delete_book(self):
      # Test deleting a book
      delete_url = reverse('book-detail', args=[self.book1.id])
      response = self.client.delete(delete_url)
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertEqual(Book.objects.count(), 1)
