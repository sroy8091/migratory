from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ContractForm, DownloadForm, BirdForm
from .models import Bird


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def download(request):
    form = ContractForm(request.POST or None)
    species = None
    end_date = None
    download_form = None

    if request.method == 'POST':
        if form.is_valid():
            # species = form.cleaned_data.get('species')
            state = form.cleaned_data.get('state')
            end_date = form.cleaned_data.get('end_date')
            iba_code = form.cleaned_data.get('iba_code')
            forest_type = form.cleaned_data.get('forest_type')
            # contracts = Bird.objects.filter(species=form.cleaned_data.get('species')).\
            #     filter(state=form.cleaned_data.get('state')).filter()
            species = Bird.objects.filter(end_date__range=["2017-02-01", end_date])
            # print(contracts)

        download_form = DownloadForm(initial={
            # 'species': species,
            'state': state,
            'end_date':end_date,
            'iba_code':iba_code,
            'forest_type':forest_type,
        })
    # print (download_form)
    # print (species)
    return render(request, 'download.html', {'form': form,
                                             'contracts': species,
                                             'download_form': download_form})


def get_csv_data(starting_date, ending_date):
    """
    Prepare data in csv format for download.
    * This is called by ``download_data`` to perform the query.
    * Do your query here and format the results as CSV using a csv
      writer or manually.
    * For this example, we're using some dummy data.
    """
    data = []
    num = 10
    for n in range(num):
        person = 'Person {}'.format(n + 1)
        type_contract = 'Some contract'
        start_date = starting_date
        end_date = ending_date
        data.append(', '.join([start_date, end_date, person, type_contract]))
    return '\n'.join(data)


def download_data(request):
    """
    Process a request to download data.
    * POST must contain 'starting_date' and 'ending_date'.
    """
    from django.http import HttpResponse

    try:
        if request.method == 'POST':
            form = DownloadForm(request.POST)
            if form.is_valid():
                species = form.cleaned_data.get('species')
                state = form.cleaned_data.get('state')
                ending_date = form.cleaned_data.get('ending_date')
                # assert species and state
                contracts = get_csv_data(species, state)
                # assert contracts
    except:
        error = 'Your request has some problems.'
        contracts = error

    attachment = 'bird_data.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(attachment)
    return response


'''
The basic idea is that:

When you render the contract search results from a query, you just add an additional
DownloadForm instance to the page.
This shows up only as a Download button,
but it contains hidden fields for the starting_date and ending_date.
When the user clicks on the Download button,
the form gets submitted to a new view called download_data that examines the request.
POST dict and extracts the starting_date and  ending_date.
Then, it prepares the queryset data and renders it in CSV format.
The download_data view then returns the response as an attachment with content-type text/csv.
The user's browser will handle that as a download file automatically.

'''

@login_required
def upload(request):

    if request.method=='POST':
        form = BirdForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('Succcess')
        else:
            d = form.cleaned_data
            print(form.errors)
            return HttpResponse('Not Uploaded')

    else:
        form = BirdForm()
        return render(request, 'upload.html',{'form': form})