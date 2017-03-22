from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import EventFormForm


def Event_form_view(request):
    if request.method == 'POST':
        form = EventFormForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')  # has to be changed according to design
    else:
        form = EventFormForm()

    context = {
        'form': form
    }

    return render(request, 'forms.html', context)


def thanks(request):
    pass
