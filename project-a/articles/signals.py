from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Article, AuditLog


@receiver(post_save, sender=Article)
def article_saved(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="create",
            article=instance,
            user=instance.author,
            summary={
                "title": instance.title,
                "status": instance.status,
            }
        )
    else:
        AuditLog.objects.create(
            action="update",
            article=instance,
            user=instance.author,
            summary={
                "status": instance.status,
            }
        )


@receiver(pre_delete, sender=Article)
def article_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        action="delete",
        article=None,
        user=instance.author,
        summary={
            "title": instance.title,
            "status": instance.status,
        }
    )