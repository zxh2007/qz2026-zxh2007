from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.db.models import F

from .models import Article


def article_detail(request, article_id):
    Article.objects.filter(
        id=article_id
    ).update(
        views=F("views") + 1
    )

    article = get_object_or_404(
        Article,
        id=article_id
    )

    return HttpResponse(
        f"{article.title}<br>浏览量：{article.views}"
    )