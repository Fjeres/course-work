from django.shortcuts import render, redirect


from basdate.settings import BASE_DIR
import os

from .models import Cars, CarModel, Accessories, AddServices, CarShowroom, Feedback, Vacancies, RequestCar
from .forms import FeedbackForm, RequestCarForm

# PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



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
    print(cars_item.photo.url)
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
            return redirect('pdf')
    else:
        form = RequestCarForm()
    return render(request, 'cars/request_car.html', {"form": form})


def render_pdf_view(request):
    request_car = RequestCar.objects.last()
    # template_path = 'cars/pdf1.html'
    template_path = 'cars/pdf1.html'
    context = {'request_car': request_car}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # если скачивать надо раскоменить нижнее
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'),  encoding='UTF-8', dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
