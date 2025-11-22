"""Signal handlers for the `core` app.

Currently logs when a `CustomModel` instance is created or updated.
"""

from typing import Any

import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomModel

logger = logging.getLogger('core')


@receiver(post_save, sender=CustomModel)
def custommodel_post_save(sender: Any, instance: CustomModel, created: bool, **kwargs: Any) -> None:
    """Log creation and updates of `CustomModel` instances.

    Args:
        sender: The model class sending the signal.
        instance: The instance that was saved.
        created: True if the instance was created.
    """
    if created:
        logger.info(f'CustomModel created: {instance.pk} {instance.title}')
    else:
        logger.info(f'CustomModel updated: {instance.pk} {instance.title}')
