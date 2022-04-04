from django.shortcuts import render


def card(request):
    return render(request, template_name='main/card.html')
