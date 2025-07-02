from django.urls import path

from news_app.views import news_list_view, NewsListView, news_deteil_view, contact_view, local_news_view

urlpatterns = [
    path('', news_list_view, name='news_list'),
    # path('', NewsListView.as_view(), name='news_list'),
    path('contact/', contact_view, name='contact'),
    path('local/', local_news_view, name='local_news'),
    path('<slug>/', news_deteil_view, name='news_detail'),
]
