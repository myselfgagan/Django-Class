from django.urls import URLPattern, path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"), # to run class based view as function by adding .as_view
    path('<int:id>', ArticleDetailView.as_view(), name="article_detail"),
    path('create', ArticleCreateView.as_view(), name="article_create"),
    path('update/<int:id>', ArticleUpdateView.as_view(), name="article_update"),
    path('delete/<int:id>', ArticleDeleteView.as_view(), name="article_delete")
]