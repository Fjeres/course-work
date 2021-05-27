from django.contrib import admin

from .models import News, Category, GeneralInformation


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', "title")
    search_fields = ("title", 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', "title")
    search_fields = ("title",)


class GeneralInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', "title")
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GeneralInformation, GeneralInformationAdmin)
