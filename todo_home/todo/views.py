from django.shortcuts import render

def home(request):
    return render(request, 'todo/home.html')


def about(request):
    return render(request, 'todo/about.html')
