from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Cars, CarModel, Accessories, AddServices, CarShowroom, Feedback, Vacancies
from .forms import FeedbackForm, RequestCarForm


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


def get_accessories(request):
    accessories = Accessories.objects.all()
    return render(request, 'cars/accessories.html',
                  {
                      'accessories': accessories,
                  })


def get_add_services(request):
    add_services = AddServices.objects.all()
    return render(request, 'cars/AddServices.html',
                  {
                      'add_services': add_services,
                  })


def get_cars_showrooms(request):
    car_showroom = CarShowroom.objects.all()
    feedback = Feedback.objects.all()
    vacancies = Vacancies.objects.all()
    return render(request, 'cars/carshowroom.html',
                  {
                      'car_showroom': car_showroom,
                      'feedback': feedback,
                      'vacancies': vacancies,
                  })


def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showrooms')
    else:
        form = FeedbackForm()
    return render(request, 'cars/add_feedback.html', {"form": form})


def add_request_car(request):
    if request.method == 'POST':
        form = RequestCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = RequestCarForm()
    return render(request, 'cars/request_car.html', {"form": form})
