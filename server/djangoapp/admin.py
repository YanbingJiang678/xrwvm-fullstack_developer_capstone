from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
# admin.site.register(CarModel)

# CarModelAdmin class
# admin.site.register(CarMake)

# CarMakeAdmin class with CarModelInline

# Register models here


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')