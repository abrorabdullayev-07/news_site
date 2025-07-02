from django.shortcuts import render
from django.views.generic import ListView
from unicodedata import category

from news_app.models import News


def news_list_view(request):
    news_list = News.published.all()

    contex = {
        'news_list' : news_list
    }

    return render(request, 'index.html', contex)


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'


def news_deteil_view(request, slug):
    news = News.objects.get(slug=slug)
    contex = {
        'news' : news
    }

    return render(request, 'single_page.html', contex)


def contact_view(request):
    return render(request, 'contact.html')

def local_news_view(request):
    news_list = News.published.filter(category__name = 'Mahalliy')
    context = {'news_list' : news_list}
    return render(request,'local_news.html', context)