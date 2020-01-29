from django.urls import path,include
from . import views
from .router import router
urlpatterns = [
    path(r'',views.ShowCarsView.as_view(), name='base'),
    path(r'add/',views.CreateCarView.as_view(), name='add_car'),
    path(r'cars-detail/<int:pk>/',views.CarsDetailView.as_view(), name='cars_detail'),
    path(r'reservation/<car_id>/',views.ReservationAdd.as_view(),name='reservvvv'),
    path(r'reservation-detail/<int:pk>/',views.ReservationDetailView.as_view(), name='reserv_detail'),
    path('api/', include(router.urls)),  # api

    path(r'', include('django.conf.urls.i18n')),
]
