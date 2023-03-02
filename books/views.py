from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView

from .models import Book
from .forms import BookForm


class BookListView(ListView):

    model = Book
    queryset = Book.objects.all()


class BookDetailView(UpdateView, DetailView):

    model = Book
    form_class = BookForm
    success_url = '/books/'
    template_name = 'books/book_detail.html'

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('book-detail', kwargs={'pk': pk})

    # def get_form(self, form_class=None):
    #     return form_class(**self.get_form_kwargs())
    #
    # def form_valid(self, form):
    #     form.save()
    #     return super(BookDetailView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(BookDetailView, self).get_context_data(**kwargs)
    #     context['form'] =
