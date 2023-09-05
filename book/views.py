from django.shortcuts import render
from .models import Book
from reader.forms import ReaderForm
from reader.models import Reader


def books(request):
    form = ReaderForm(request.POST)
    if form.is_valid():
        form.save()
        all_books = Book.objects.all()
        return render(request, "book_list.html", {"data": all_books})
    else:
        form = ReaderForm()
    return render(request, template_name='reader_auth.html', context={'form': form})



