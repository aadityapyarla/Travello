from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html' ,{'name': 'Aaditya', 'whose': 'My'})

def add(request):
    num1 = int(request.POST.get('text1'))
    num2 = int(request.POST.get('text2'))
    result = num1 + num2
    return render(request, 'result.html', {'name':result})

