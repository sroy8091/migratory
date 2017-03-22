from django.contrib import admin
from django.http import HttpResponse
from .models import EventForm
from .forms import EventFormForm

# Register your models here.

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=dev_ic.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Name"),
        smart_str(u"Paper_ID"),
        smart_str(u"Title"),
        smart_str(u"Address"),
        smart_str(u"Email"),
        smart_str(u"Contact"),
        smart_str(u"Amount"),
        smart_str(u"Bank"),
        smart_str(u"Reference_Number"),
        smart_str(u"Date_of_Fee_Deposited"),
        smart_str(u"Accommodation"),
        smart_str(u"Food_Choice"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.Name),
            smart_str(obj.Paper_ID),
            smart_str(obj.Title),
            smart_str(obj.Address),
            smart_str(obj.Email),
            smart_str(obj.Contact),
            smart_str(obj.Amount),
            smart_str(obj.Bank),
            smart_str(obj.Reference_Number),
            smart_str(obj.Date_of_Fee_Deposited),
            smart_str(obj.Accommodation),
            smart_str(obj.Food_Choice),
        ])
    return response
export_csv.short_description = u"Export CSV"

class EventFormAdmin(admin.ModelAdmin):
    actions = [export_csv]
    list_display=["Name",'Title','Email']
    form = EventFormForm


admin.site.register(EventForm, EventFormAdmin)
