from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):

    all_books = Book.objects.all().order_by("-rating")

    total_number_of_books = all_books.count()
    average_rating = all_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "all_books": all_books,
        "total_number_of_books": total_number_of_books,
        "average_rating": average_rating,
    })

def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()

    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })