"""App configuration for the `core` application."""

from typing import Any

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self) -> None:
        """Import signal handlers when the app registry is ready.

        Importing `core.signals` here ensures signal receivers are
        registered at startup without importing models too early.
        """
        # Import signals to ensure they're registered
        import core.signals  # noqa: F401
