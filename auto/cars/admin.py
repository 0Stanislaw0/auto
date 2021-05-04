from django.contrib import admin
from .models import Cars,Reservations_cars


class CarsEdit(admin.ModelAdmin):
    list_display = ('id','nameru', 'nameen', 'year_of_creation')
    list_display_links = ('nameru', 'year_of_creation')
    search_fields = ('nameru', 'year_of_creation')

class ReservEdit(admin.ModelAdmin):
    list_display = ('car', 'start_time', 'end_time')
    list_display_links = ('start_time', 'end_time')
    search_fields = ('start_time','car',)

admin.site.register(Reservations_cars, ReservEdit)
admin.site.register(Cars, CarsEdit)



