from django.contrib import admin

# Register your models here.
from .models import Observation, Iba, State, contribution
from .forms import Observation_form


class BirdAdmin(admin.ModelAdmin):
    # def get_fieldsets(self, request, obj=None):
    #     form = BirdForm
    #     return [(None, {'fields': form.base_fields.keys()})]
    search_fields = ['species']
    raw_id_fields = ['species']
    # form = BirdForm

admin.site.register(Observation)
admin.site.register(Iba)
admin.site.register(State)
admin.site.register(contribution)