from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='cars'),
    path('models/<int:car_model_id>/', get_car_model, name='models'),
    path('cars/<int:cars_id>/', view_cars, name='view_cars'),
]
