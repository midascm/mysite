from django.templatetags.static import static
from django.shortcuts import get_object_or_404, render
from .models import Article

def index(req):
    latest_article_list = Article.objects.all().order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(req, 'news/index.html', context)

def detail(req, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(req, 'news/detail.html', { 'article': article })

def results(req):
    context = {

    }
    return render(req, 'news/results.html', context=context)
