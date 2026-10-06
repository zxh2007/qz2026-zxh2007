from django.urls import path

from .views import article_detail

urlpatterns = [
    path(
        "article/<int:article_id>/",
        article_detail,
        name="article_detail"
    ),
]