from django.shortcuts import render
from webapp.models import Article
# Create your views here.


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'create_article.html')
    elif request.method == "POST":
        article = Article.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            body=request.POST.get('body')
        )
        articles = Article.objects.all()

        # context = {
        #     'title': request.POST.get('title'),
        #     'author': request.POST.get('author'),
        #     'body': request.POST.get('body')
        # }

        return render(request, 'article_list.html', context={
            'articles': articles
        })

def article_list_view(request):
    articles = Article.objects.all()

    return render(request, 'article_list.html', context={
        'articles': articles
    })
