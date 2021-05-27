from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='cars'),
    path('models/<int:car_model_id>/', get_car_model, name='models'),
    path('<int:cars_id>/', view_cars, name='view_cars'),
    path('accessories/', get_accessories, name='accessories'),
    path('services/', get_add_services, name='services'),
    path('showrooms/', get_cars_showrooms, name='showrooms'),
    path('add-feedback/', add_feedback, name='add_feedback'),
    path('add-request/', add_request_car, name='request_car'),
]
