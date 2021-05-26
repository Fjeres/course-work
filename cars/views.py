from django.shortcuts import render

from django.http import HttpResponse
from .models import Cars, CarModel


def index(request):
    cars = Cars.objects.all()
    return render(request, 'cars/index.html',
                  {
                      "cars": cars,
                      'title': "Автомобильный ряд",

                  })


def get_car_model(request, car_model_id):
    cars = Cars.objects.filter(carModel_id=car_model_id)

    car_model = CarModel.objects.get(pk=car_model_id)
    return render(request, 'cars/model.html',
                  {
                      "cars": cars,

                      'car_model': car_model,

                  })


def view_cars(request, cars_id):
    cars_item = Cars.objects.get(pk=cars_id)
    return render(request, 'cars/view_cars.html',
                  {
                      "cars_item": cars_item
                  })
