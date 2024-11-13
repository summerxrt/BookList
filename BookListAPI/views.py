from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect

def home(request):
    return HttpResponse("<h1>Welcome to the Book List API!</h1><p>Go to <a href='/api/books'>/api/books</a> to see the available books.</p>")

# Optional: Redirect view if you want to redirect from root to /api/books directly
def home_redirect(request):
    return redirect('/api/books')


@csrf_exempt
def books(request):
    if request.method == 'GET':
        # Fetch all books from the database and convert them to a list of dictionaries
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)}, safe=False)

    elif request.method == 'POST':
        # Retrieve data from POST request
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        # Create a new Book object
        try:
            book = Book(title=title, author=author, price=price)
            book.save()  # Save the book instance to the database
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        # Return a JSON response with the saved book data
        return JsonResponse(model_to_dict(book), status=201)

