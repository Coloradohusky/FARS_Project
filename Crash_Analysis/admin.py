from django.contrib.gis import admin

# Register your models here.
from .models import Accident, Vehicle, Person

# admin.site.register(Accident)

@admin.register(Accident)
class AccidentAdmin(admin.GISModelAdmin):
    list_display = ("st_case", "location")

admin.site.register(Vehicle)
admin.site.register(Person)