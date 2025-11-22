"""Context processors providing global template context values."""

from typing import Any, Dict


def global_settings(request: Any) -> Dict[str, Any]:
    """Return global values available in all templates.

    Args:
        request: The current HttpRequest (unused here but included for API compatibility).

    Returns:
        A mapping of context names to values.
    """
    return {
        'site_name': 'Customization Demo',
        'global_value': 12345,
    }
