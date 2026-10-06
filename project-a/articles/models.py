from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    STATUS_CHOICES = [
        ("draft", "草稿"),
        ("published", "已发布"),
        ("archived", "已归档"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title


class Attachment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="attachments"
    )

    filename = models.CharField(max_length=200)

    file = models.FileField(
        upload_to="attachments/"
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "附件"
        verbose_name_plural = "附件"

    def __str__(self):
        return self.filename


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ("create", "创建"),
        ("update", "修改"),
        ("publish", "发布"),
        ("archive", "归档"),
        ("delete", "删除"),
    ]

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    summary = models.JSONField(default=dict)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "审计日志"
        verbose_name_plural = "审计日志"

    def __str__(self):
        return self.action