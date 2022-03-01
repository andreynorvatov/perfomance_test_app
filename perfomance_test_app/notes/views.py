from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import Notes
from .utils import *
from .forms import NotesForm
from django.db.models import Q

from django.core.paginator import Paginator


def notes_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        notes = Notes.objects.filter(Q(title__icontains=search_query) |
                                     Q(body__icontains=search_query))
    else:
        notes = Notes.objects.all()

    paginator = Paginator(notes, 30)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'index.html', context=context)


class NotesDetail(ObjectDetailMixin, View):
    model = Notes
    template = 'notes_detail.html'


class NotesCreate(ObjectCreateMixin, View):
    model_form = NotesForm
    template = 'notes_create_form.html'
    raise_exception = True


class NotesUpdate(ObjectUpdateMixin, View):
    model = Notes
    model_form = NotesForm
    template = 'notes_update_form.html'
    raise_exception = True


class NotesDelete(ObjectDeleteMixin, View):
    model = Notes
    template = 'notes_delete_form.html'
    redirect_url = 'notes_list_url'
    raise_exception = True
