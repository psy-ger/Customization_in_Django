from django.forms import widgets


class FancySelect(widgets.Select):
    template_name = 'core/widgets/fancy_select.html'

    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
