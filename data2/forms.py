from django import forms
from .models import EventForm

class EventFormForm(forms.ModelForm):
    #full_name = forms.CharField(label="Your Name:" , max_length=30)
    class Meta:
        """docstring for Meta."""
        model=EventForm
        fields = ['Name' ,'Paper_ID' ,'Title','Address','Email','Contact', 'Amount', 'Bank', 'Reference_Number',
                  'Date_of_Fee_Deposited', 'Accommodation', 'Food_Choice']
        def __init__(self, arg):
            super(Meta, self).__init__()
            self.arg = arg
