from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def education(request):
    return render(request, 'main/education.html')


def office(request):
    return render(request, 'main/office.html')


def home(request):
    return render(request, 'main/home.html')