from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Observation
from account.models import user


class ContractForm(forms.Form):
    end_date = forms.DateField(widget=AdminDateWidget)
    state = forms.CharField()
    iba_code = forms.BooleanField(required=False)
    forest_type = forms.BooleanField(required=False)


class DownloadForm(forms.Form):
    # species = forms.CharField(widget=forms.HiddenInput)
    state = forms.CharField(widget=forms.HiddenInput)


class Observation_form(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['iba_code', 'start', 'duration', 'protocol_type', 'trip_comments']


class Observation_edit_form(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['iba_code', 'start', 'duration', 'protocol_type', 'trip_comments']

