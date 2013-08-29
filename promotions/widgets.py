from django.forms import Widget, TextInput, DateInput
from django.forms.util import flatatt
from django.forms.widgets import CheckboxInput

from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class AceInputBox(TextInput):

    def label_tag(self, contents=None, attrs=None):
        pass

    def render(self, name, value, attrs=None):
        result = super(AceInputBox, self).render(name, value, attrs)
        return result


class AceDateBox(DateInput):
    def render(self, name, value, attrs=None):
        result = super(AceDateBox, self).render(name, value, attrs)
        return mark_safe(
            """
            <div class="row-fluid input-append">
                %s
                <span class="add-on">
                <i class="icon-calendar"></i>
            </span>
            </div>
            """ % result)


class AceCheckBox(CheckboxInput):
    def render(self, name, value, attrs=None):
        result = super(AceCheckBox, self).render(name, value, attrs)
        return """
                %s
                <span class="lbl"></span>
            """ % result
