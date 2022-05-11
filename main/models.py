from django.db import models


class District(models.Model):
    """
    Районы Москвы
    """

    name = models.CharField('Название района', max_length=255)

    class Meta:
        verbose_name = 'Район Москвы'
        verbose_name_plural = 'Районы Москвы'


class Category(models.Model):
    """
    Категория объекта культурного наследия
    """

    name = models.CharField('Название категории', max_length=255)

    class Meta:
        verbose_name = 'Категория объекта культурного наследия'
        verbose_name_plural = 'Категории объектов культурного наследия'


class TypeObject(models.Model):
    """
    Типы объектов культурного наследия
    """

    name = models.CharField('Название типа объекта', max_length=255)

    class Meta:
        verbose_name = 'Тип объекта культурного наследия'
        verbose_name_plural = 'Типы объектов культурного наследия'


class StatusObject(models.Model):
    """
    Статус объекта культурного наследия
    """

    name = models.CharField('Статус объекта', max_length=255)

    class Meta:
        verbose_name = 'Категория объекта культурного наследия'
        verbose_name_plural = 'Категории объектов культурного наследия'


class CultureObjects(models.Model):
    """
    Объекты культурного наследия.
    """

    name = models.CharField(
        'Название объекта',
        max_length=255,
    )
    ensemble_name_on_doc = models.CharField(
        'Название объекта в документах',
        max_length=255,
    )
    adm_area = models.CharField(
        'Административный округ',
        max_length=255,
    )
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    location = models.CharField(
        'Локация',
        max_length=255,
    )
    addresses = models.CharField(
        'Адрес',
        max_length=255,
    )
    status = models.ForeignKey(
        StatusObject,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    type = models.ForeignKey(
        TypeObject,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    long_position = models.DecimalField(
        max_digits=8,
        decimal_places=3,
    )
    lat_position = models.DecimalField(
        max_digits=8,
        decimal_places=3,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект культурного наследия'
        verbose_name_plural = 'Объекты культурного наследия'
