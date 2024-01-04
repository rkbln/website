from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def article_create_view(request):
    if request.method == "GET":
        return render(request, 'create_article.html')
    elif request.method == "POST":
        context = {
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'body': request.POST.get('body')
        }
        return render(request, 'article.detail.html', context)