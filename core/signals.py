from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomModel
import logging

logger = logging.getLogger('core')


@receiver(post_save, sender=CustomModel)
def custommodel_post_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f'CustomModel created: {instance.pk} {instance.title}')
    else:
        logger.info(f'CustomModel updated: {instance.pk} {instance.title}')
