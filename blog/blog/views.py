from django.shortcuts import render, get_object_or_404

from blog.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def article(request, article_id):
    article_ = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article_': article_})