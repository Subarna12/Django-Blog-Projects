from django.urls import path
from .views import articles_list, article_create, article_detail

app_name = 'articles'

urlpatterns = [
    path('', articles_list, name='list'),
    path('create/', article_create, name="create"),
    path('<slug:slug>/', article_detail, name="detail")
]
