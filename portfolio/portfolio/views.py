from __future__ import unicode_literals
from django.shortcuts import render


def index_page(request):
    return render(request, 'index.html')
