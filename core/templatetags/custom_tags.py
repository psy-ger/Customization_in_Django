"""Custom template tags and filters for `core`.

Includes a simple `current_year` tag, an `uppercase` filter and a small
helper tag `render_stats` that renders basic statistics for an object.
"""

from typing import Any, Dict

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def current_year() -> int:
    """Return the current year as an integer."""
    from datetime import datetime

    return datetime.now().year


@register.filter
def uppercase(value: Any) -> str:
    """Return the input converted to uppercase (safely handle None)."""
    if value is None:
        return ''
    return str(value).upper()


@register.simple_tag(takes_context=True)
def render_stats(context: Dict[str, Any], obj: Any) -> str:
    """Return a small HTML snippet with stats for the object.

    The tag calls `obj.stats()` when available and renders a minimal
    HTML snippet. Returned string is marked safe.
    """
    stats = getattr(obj, 'stats', lambda: {})()
    html = f"<div class=\"stats\">Words: {stats.get('words', 0)} | Keys: {stats.get('json_keys', 0)}</div>"
    return mark_safe(html)
