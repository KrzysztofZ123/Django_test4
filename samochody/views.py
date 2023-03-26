from django.shortcuts import render


def index(request):
    return render(request, 'samochody/index.html')


def duze(request):
    return render(request, 'samochody/duze.html')


def srednie(request):
    return render(request, 'samochody/srednie.html')


def male(request):
    return render(request, 'samochody/male.html')
