from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return HttpResponse('SOBRE')

def contact(request):
  return HttpResponse('CONTATO')
