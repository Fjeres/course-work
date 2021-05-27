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
        return self.carModel.title

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


class Accessories(models.Model):
    content = models.TextField(verbose_name='Описание')
    title = models.ForeignKey('CarModel', on_delete=models.PROTECT, null=True, verbose_name='Модель')

    def __str__(self):
        return self.title.title

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class AddServices(models.Model):
    name_services = models.CharField(max_length=40, verbose_name='Услуга')
    name_company = models.CharField(max_length=40, verbose_name='Компания')
    content = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name_services

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class CarShowroom(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    telephone = models.CharField(max_length=15, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'


class Feedback(models.Model):
    name = models.CharField(max_length=10, verbose_name='Имя клиента')
    сar_showroom = models.ForeignKey('CarShowroom', on_delete=models.PROTECT, null=True, verbose_name='Автосалон')
    content = models.TextField(blank=True, verbose_name='Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Vacancies(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название вакансии')
    content = models.TextField(blank=True, verbose_name='Описание')
    telephone = models.CharField(max_length=15, verbose_name='Телефон')
    сar_showroom = models.ForeignKey('CarShowroom', on_delete=models.PROTECT, null=True, verbose_name='Автосалон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class RequestCar(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    telephone = models.CharField(max_length=15, verbose_name='Телефон')
    сar_showroom = models.ForeignKey('CarShowroom', on_delete=models.PROTECT, null=True, verbose_name='Автосалон')
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, null=True, verbose_name='Автомобиль')
    services = models.ForeignKey('AddServices', blank=True, on_delete=models.PROTECT, null=True,
                                 verbose_name='Дополнительные услуги')

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
