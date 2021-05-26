from django.db import models

from django.urls import reverse


class Cars(models.Model):
    title = models.CharField(max_length=4, verbose_name='Марка', default='Lada')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/', blank=True, verbose_name='Фото')
    price = models.CharField(max_length=10, verbose_name='Цена')
    carModel = models.ForeignKey('CarModel', on_delete=models.PROTECT, null=True, verbose_name='Модель')

    def get_absolute_url(self):
        return reverse('view_cars', kwargs={"cars_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class CarModel(models.Model):
    title = models.CharField(max_length=30, db_index=True, verbose_name='Модель')

    def get_absolute_url(self):
        return reverse('models', kwargs={"car_model_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
