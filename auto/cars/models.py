from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _


class Cars(models.Model):  # Машины, которые будут размещать пользователи
	nameru = models.CharField(_('Русское название'), max_length=150)
	nameen = models.CharField(_('Английское название'), max_length=150)
	year_of_creation = models.PositiveIntegerField(_('Год создания'))
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
							   verbose_name=_('Владелец'), related_name="car")

	def get_absolute_url(self):
		return reverse('cars_detail', kwargs={'pk': self.pk})

	def __str__(self):
		lang = get_language()
		if lang == "ru":
			return '%s, %s' % (self.nameru, self.year_of_creation)
		else:
			return '%s, %s' % (self.nameen, self.year_of_creation)

	class Meta:
		verbose_name_plural = _('Автомобили')
		verbose_name = _('Автомобиль')


class Reservations_cars(models.Model):
	car = models.ForeignKey(Cars, on_delete=models.CASCADE)
	start_time = models.DateTimeField(default=timezone.now, verbose_name=_('дата аренды'))
	end_time = models.DateTimeField(default=timezone.now, verbose_name=_('дата возвращения'))
	customer = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Арендатор'))

	def get_absolute_url(self):
		return reverse('reserv_detail', kwargs={'pk': self.pk})

	class Meta:
		verbose_name_plural = _('Аренда машин')
		verbose_name = _('Аренда машины')
