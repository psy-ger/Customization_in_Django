from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def current_year():
    from datetime import datetime
    return datetime.now().year


@register.filter
def uppercase(value):
    if value is None:
        return ''
    return str(value).upper()


@register.simple_tag(takes_context=True)
def render_stats(context, obj):
    """Return a small HTML snippet with stats for the object."""
    stats = getattr(obj, 'stats', lambda: {})()
    html = f"<div class=\"stats\">Words: {stats.get('words', 0)} | Keys: {stats.get('json_keys', 0)}</div>"
    return mark_safe(html)
