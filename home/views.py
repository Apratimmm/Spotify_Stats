from django.shortcuts import render

def homepage(request):
    return render(request,'home/home.html')

def error_page(request):
    return render(request, 'home/error.html')
