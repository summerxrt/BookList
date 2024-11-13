from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books, name='books'),  # This will route /api/books to the books view function
]
