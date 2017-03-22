from django.contrib import admin

# Register your models here.
from .models import Bird
from .forms import BirdForm


class BirdAdmin(admin.ModelAdmin):
    # def get_fieldsets(self, request, obj=None):
    #     form = BirdForm
    #     return [(None, {'fields': form.base_fields.keys()})]
    form = BirdForm

admin.site.register(Bird, BirdAdmin)