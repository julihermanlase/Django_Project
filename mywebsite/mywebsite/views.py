from django.shortcuts import render

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
