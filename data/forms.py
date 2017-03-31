from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Bird


class ContractForm(forms.Form):
    end_date = forms.DateField(widget=AdminDateWidget)
    state = forms.CharField()
    iba_code = forms.BooleanField(required=False)
    forest_type = forms.BooleanField(required=False)


class DownloadForm(forms.Form):
    # species = forms.CharField(widget=forms.HiddenInput)
    state = forms.CharField(widget=forms.HiddenInput)


class BirdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BirdForm, self).__init__(*args, **kwargs)
        type_of_loc = (('BREEDING POINT', 'BREEDING POINT'), ('STOPPING POINT', 'STOPPING POINT'))
        self.fields['type_of_location'] = forms.ChoiceField(choices=type_of_loc, widget=forms.RadioSelect())
        self.fields['start_date'] = forms.DateField(widget=AdminDateWidget)
        self.fields['end_date'] = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Bird
        fields = '__all__'
