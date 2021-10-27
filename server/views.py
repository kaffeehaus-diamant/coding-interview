
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return render(request, 'server/index.html')
