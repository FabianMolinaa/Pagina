from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mi_vista(request):
    return render(request, 'index.html')