from .models import Cars, Reservations_cars
from django import forms
from django.utils.translation import ugettext_lazy as _


class ReservationAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.car = kwargs.pop('car')
        super().__init__(*args, **kwargs)

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (
                new_end >= fixed_start and new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")
        if end <= start:
            raise forms.ValidationError(_('Ending times must after starting times'))

        reservations = Reservations_cars.objects.filter(car=self.car)
        if reservations.exists():
            for reserv in reservations:
                if self.check_overlap(reserv.start_time, reserv.end_time, start, end):
                    raise forms.ValidationError(_(
                        'There is an overlap with another reserv: ' + str(reserv.car.nameen) + ', ' + str(
                            reserv.start_time.strftime("%d.%m.%Y")) + ' - ' + str(reserv.end_time.strftime("%d.%m.%Y"))))

    class Meta:
        model = Reservations_cars
        fields = ('start_time', 'end_time')


class CarsAddForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ("author", 'nameru', 'nameen', 'year_of_creation')
