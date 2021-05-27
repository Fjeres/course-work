from django.shortcuts import render

from django.http import HttpResponse
from .models import News, Category, GeneralInformation


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html',
                  {
                      'news': news,
                      'title': "Список новостей",
                  })


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html',
                  {
                      'news': news,
                      'category': category,
                  })


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html',
                  {
                      "news_item": news_item
                  })


def get_general_information(request):
    information = GeneralInformation.objects.all()
    return render(request, 'news/information.html',
                  {
                      "information": information,
                      'title': "Главная",
                  })
