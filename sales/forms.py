from django import forms

from .constants import DRINKS_PRICE
from .models import Drink, Staff

class SaleForm(forms.ModelForm):

    def get_name_choices(self):
        DRINKS = [(str(k), k) for k in DRINKS_PRICE.keys()]
        return DRINKS

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ChoiceField(
            choices=self.get_name_choices()
        )

    class Meta:
        model = Drink
        fields = ['name', 'price_per_cup', 'sold_by']
        widgets = {'price_per_cup': forms.HiddenInput()}


class ReportForm(forms.Form):
    Start_date = forms.DateField(label='Start Date',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    End_date = forms.DateField(label='End Date',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    User = forms.CharField(label='Name of staff member')

    def get_user_choices(self):
        return [(str(k), k) for k in Staff.objects.all()]



    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['User'] = forms.ChoiceField(
            choices=self.get_user_choices()
        )