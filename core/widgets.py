"""Custom form widgets for the `core` app."""

from typing import Any, Iterable, Optional

from django.forms import widgets


class FancySelect(widgets.Select):
    """A simple custom Select widget that uses a dedicated template.

    The widget is thin — template controls visual representation.
    """

    template_name = 'core/widgets/fancy_select.html'

    def __init__(self, attrs: Optional[dict] = None, choices: Iterable[Any] = ()) -> None:
        super().__init__(attrs, choices)
