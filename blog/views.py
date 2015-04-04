from django.shortcuts import render
from .models import Article
from django.http import Http404
# Create your views here.


def index(request):
    articles = Article.objects.order_by('-created')
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    try:
        slug = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise Http404("Articles Doesnt Exist")
    return render(request, 'blog/detail.html', {'article': slug})