from django.contrib import admin

from .models import Cars, CarModel, Accessories, AddServices, CarShowroom, Feedback, Vacancies, RequestCar


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'carModel', 'price')
    list_display_links = ('id',)
    search_fields = ("title", 'content')


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', "title")
    search_fields = ("title",)


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', "title")
    search_fields = ("title",)


class AddServicesAdmin(admin.ModelAdmin):
    list_display = ('name_services', 'name_company')
    list_display_links = ("name_company",)
    search_fields = ("name_services", 'name_company')


class CarShowroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'telephone',)
    list_display_links = ("name",)
    search_fields = ("name",)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'сar_showroom')
    list_display_links = ("name",)


class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'сar_showroom')
    list_display_links = ("name",)


class RequestCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'telephone',)
    list_display_links = ('surname', 'id')


admin.site.register(Cars, CarsAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(AddServices, AddServicesAdmin)
admin.site.register(CarShowroom, CarShowroomAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(RequestCar, RequestCarAdmin)
