from django.contrib import admin
from .models import Book

# Customize the Book model in the Django admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Add a search bar to search by title and author
    list_filter = ('author',)  # Add a filter to filter books by author

# Register the Book model using BookAdmin for enhanced admin functionality
admin.site.register(Book, BookAdmin)
