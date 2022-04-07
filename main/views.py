from django.contrib.auth import login
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from forms import SigUpForm
from main.models import Post


class MainView(View):
    """ home page render """
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'main/homepage.html', context={'page_obj': page_obj})


class PostDetailView(View):
    """ get full post information after push detail button """
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'main/post_detail.html', context={'post': post})


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'main/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'main/signup.html', context={
            'form': form,
        })


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

