from django.urls import path
from .views import (ArticleListView, ArticleDeleteView, ArticleDetailView,
                    ArticleEditView)

urlpatterns = [
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(),
         name='article_delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='article_list')
]
