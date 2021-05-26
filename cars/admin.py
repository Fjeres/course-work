from django.contrib import admin

from .models import Cars, CarModel


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'carModel', 'price')
    list_display_links = ('id',)
    search_fields = ("title", 'content')


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', "title")
    search_fields = ("title",)


admin.site.register(Cars, CarsAdmin)
admin.site.register(CarModel, CarModelAdmin)
