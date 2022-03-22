from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView
from .forms import CreateBookForm
from django.conf import settings


class ListBookView(ListView):
    model = Book

    def get(self, request, *args, **kwarg):
        template_name = 'books/list_books.html'
        obj = {
            'books': Book.objects.all(),
            'media_url': settings.MEDIA_URL
        }
        return render(request, template_name, obj)


class CreateBookView(CreateView):
    template_name = 'books/create_book.html'
    form_class = CreateBookForm
    success_message = 'Crate Post successfully!'


class DetailBookView(View):
    model = Book
    template_name = 'books/detail.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/detail.html', {'book': book})


class UpdateBookView(UpdateView):
    template_name = 'books/edit_book.html'
    model = Book
    fields = ['name', 'author', 'publisher', 'release_date', 'price', 'image']


def delete_book(request, pk):
    post = Book.objects.filter(id=pk)
    post.delete()
    context = {
      "message": "Delete Book successfully",
      'books': Book.objects.all()
    }
    return render(request, 'books/list_books.html', context)