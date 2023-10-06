from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def use_api(request):
    return render(request, 'use_api.html')

def contact(request):
    return render(request, 'contact.html')

def data_preview(request):
    return render(request, 'data_preview.html')
