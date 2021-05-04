from .serializers import CarsSerializer
from .models import Cars, Reservations_cars
from .forms import ReservationAddForm

from rest_framework.response import Response
from rest_framework import viewsets

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin
from django.views.generic import (
    ListView,  # позволяет перебирать список базы данных и можем выводить на экра
    DetailView,  # позволяет работать с одной  статьей
    CreateView,
    UpdateView,  # обновляем данные
)
from django.utils.translation import get_language


## Api Cars


class CarsView(viewsets.ModelViewSet):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()

    def list(self, request):
        queryset = Cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cars.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CarsSerializer(user)
        return Response(serializer.data)


## Cars

class CreateCarView(LoginRequiredMixin, CreateView):
    model = Cars
    fields = ['nameru', 'nameen', 'year_of_creation']
    template_name = 'cars/cars_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        my_mail = settings.EMAIL_HOST_USER
        data = """
        Hello there!
         You add car to system!
        ~ Configs
            """
        send_mail('Welcome!', data, my_mail, [self.request.user.email])
        return super().form_valid(form)


class CarsDetailView(LoginRequiredMixin, DetailView):
    model = Cars
    template_name = 'cars/cars_detail.html'


class UpdateCarsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cars
    fields = ['nameru', 'nameen', 'year_of_creation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cars = self.get_object()
        if self.request.user == cars.author:  # проверяем авторизованного пользователя и  Владельца
            return True
        return False


class ShowCarsView(LoginRequiredMixin, ListView):
    model = Cars
    template_name = 'cars/cars_models.html'  # задаем адрес
    context_object_name = 'cars'
    ordering = ['-date']
    paginate_by = 4

    def test_func(self):
        cars = self.get_object()
        if self.request.user == cars.author:
            return True
        return False


## Reservations


class ReservationAdd(LoginRequiredMixin, CreateView):
    template_name = 'cars/reservation.html'
    model = Reservations_cars
    form_class = ReservationAddForm

    def get_form_kwargs(self):
        self.car = Cars.objects.get(pk=self.kwargs['car_id'])
        kwargs = super().get_form_kwargs()
        kwargs['car'] = self.car
        return kwargs

    def form_valid(self, form):
        form.instance.car = self.car
        form.instance.customer = self.request.user
        my_mail = settings.EMAIL_HOST_USER
        data = f"""
        Hello there!
        You have booked a car {self.car.nameen}, from {form.instance.start_time.strftime("%d.%m.%Y")} to {form.instance.end_time.strftime("%d.%m.%Y")}
        ~ Configs
            """
        send_mail('Welcome!', data, my_mail, [self.request.user.email])
        messages.success(self.request, _("Дальнейшние инструкции отправлены вам на почту!"))
        return super().form_valid(form)


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservations_cars
    template_name = 'cars/reservation_detail.html'
