from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404
from django.db.models import Avg,Max,Min
# Create your views here.

def index(request):
    books=Book.objects.all()
    c= books.count()
    avg=books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{
        "books" : books,
        "total":c,
        "average_rating":avg
    })

def book_detail(request,slug):
    book=get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_details.html",{
        "title": book.title,
        "author" : book.author,
        "rating" : book.rating,
        "is_bestseller" : book.is_bestselling
    })