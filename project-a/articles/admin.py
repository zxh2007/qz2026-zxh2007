from django.contrib import admin
from .models import Article, Attachment, AuditLog


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "status",
        "views",
        "created_at",
    )

    list_filter = (
        "status",
        "author",
    )

    search_fields = (
        "title",
    )


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "filename",
        "article",
        "uploaded_at",
    )


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "article",
        "user",
        "timestamp",
    )