from django.forms import ModelForm, DateInput, CheckboxInput
from django.forms.widgets import TextInput
from promotions.models import Promotion


class PromotionWizardDetailsPage(ModelForm):
    error_css_class = 'error'

    class Meta:
        model = Promotion
        fields = ['id', 'description', 'start_date', 'end_date', 'active']
        widgets = {
            'description': TextInput(attrs={'class': 'span8'}),
            'start_date': DateInput(attrs={'class': 'date-picker'}),
            'end_date': DateInput(attrs={'class': 'date-picker'}),
            'active': CheckboxInput(attrs={'class': 'ace ace-switch ace-switch-5'}),
        }


class PromotionWizardLayoutPage(ModelForm):
    class Meta:
        model = Promotion
        fields = ['id', 'description', 'body_text']
        widgets = {
            'description': TextInput(attrs={'class': 'span8'}),
            'body_text': TextInput(attrs={'class': 'span8'}),
        }

