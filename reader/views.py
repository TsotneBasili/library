from django.shortcuts import render, redirect
from .forms import ReaderForm


def authorization(request):
    # if request.method == 'post':
    #     form = ReaderForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('book.templates')
    # else:
    form = ReaderForm()
    return render(request, template_name='reader_auth.html', context={'form': form})
