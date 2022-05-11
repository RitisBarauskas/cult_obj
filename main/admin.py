from django.contrib import admin

from main.models import (AdmArea, Category, CultureObject, District,
                         StatusObject, TypeObject)


@admin.register(CultureObject)
class CultureObjectAdmin(admin.ModelAdmin):
    """
    Админ-панель объектов культурного наследия
    """

    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админ-панель категорий объектов культурного наследия
    """

    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    """
    Админ-панель районов Москвы
    """

    pass


@admin.register(TypeObject)
class TypeObjectAdmin(admin.ModelAdmin):
    """
    Админ-панель типов объектов
    """

    pass


@admin.register(StatusObject)
class StatusObjectAdmin(admin.ModelAdmin):
    """
    Админ-панель статусов объектов культурного наследия
    """

    pass


@admin.register(AdmArea)
class AdmAreaAdmin(admin.ModelAdmin):
    """
    Админ-панель административных округов
    """

    pass
