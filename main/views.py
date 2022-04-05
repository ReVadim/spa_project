from django.shortcuts import render


def home(request):
    return render(request, template_name='main/homepage.html')


def card(request):
    return render(request, template_name='main/card.html')


def article(request):
    return render(request, template_name='main/article.html')


def contacts(request):
    return render(request, template_name='main/contact.html')


def thanks(request):
    return render(request, template_name='main/thanks.html')


def registration(request):
    return render(request, template_name='main/registration.html')


def signup(request):
    return render(request, template_name='main/signup.html')
