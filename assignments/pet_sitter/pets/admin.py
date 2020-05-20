from django.contrib import admin
from pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('name', 'species', 'breed', 'owner')


admin.site.register(Pet, PetAdmin)