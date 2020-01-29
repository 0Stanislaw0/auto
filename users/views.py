from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from .forms import UserOurRegistration, UserUpdateForm
from cars.models import Reservations_cars, Cars
from .models import CustomUser
from .serializers import UserSerializer, UserSigninSerializer
from .authentication import token_expire_handler, expires_in


@api_view(["GET"])
def user_info(request):
    return Response({
        'user': request.user.email,
        'expires_in': expires_in(request.auth)
    }, status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def signin(request):
    signin_serializer = UserSigninSerializer(data=request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=signin_serializer.data['username'],
        password=signin_serializer.data['password']
    )
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)

    # TOKEN STUFF
    token, _ = Token.objects.get_or_create(user=user)

    # token_expire_handler will check, if the token is expired it will generate new one
    is_expired, token = token_expire_handler(token)  # The implementation will be described further
    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data,
        'expires_in': expires_in(token),
        'token': token.key
    }, status=HTTP_200_OK)

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


def registr(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Пользователь {email} был успешно создан, войдите в аккаунт.')
            return redirect('login')
    else:
        form = UserOurRegistration()

    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.user.is_authenticated:
        cars = Cars.objects.filter(author=request.user)
        reservations = Reservations_cars.objects.filter(customer=request.user)
        if request.method == "POST":
            update_user = UserUpdateForm(request.POST, instance=request.user)
            if update_user.is_valid:
                update_user.save()
                messages.success(request, f'Данные успешно изменены.')
                return redirect('login')
        else:
            update_user = UserUpdateForm(instance=request.user)
        data = {
            'update_user': update_user,
            'reservations': reservations,
            'cars': cars
        }
        return render(request, 'users/profile.html', data)
    else:
        redirect('login')
