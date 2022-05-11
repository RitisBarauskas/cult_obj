from django.db import models


class District(models.Model):
    """
    Районы Москвы
    """

    name = models.CharField('Название района', max_length=255)

    class Meta:
        verbose_name = 'Район Москвы'
        verbose_name_plural = 'Районы Москвы'

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Категория объекта культурного наследия
    """

    name = models.CharField('Название категории', max_length=255)

    class Meta:
        verbose_name = 'Категория объекта культурного наследия'
        verbose_name_plural = 'Категории объектов культурного наследия'

    def __str__(self):
        return self.name


class TypeObject(models.Model):
    """
    Типы объектов культурного наследия
    """

    name = models.CharField('Название типа объекта', max_length=255)

    class Meta:
        verbose_name = 'Тип объекта культурного наследия'
        verbose_name_plural = 'Типы объектов культурного наследия'

    def __str__(self):
        return self.name


class StatusObject(models.Model):
    """
    Статус объекта культурного наследия
    """

    name = models.CharField('Статус объекта', max_length=255)

    class Meta:
        verbose_name = 'Категория объекта культурного наследия'
        verbose_name_plural = 'Категории объектов культурного наследия'

    def __str__(self):
        return self.name


class AdmArea(models.Model):
    """
    Административный округ Москвы
    """

    name = models.CharField('Административный округ', max_length=255)

    class Meta:
        verbose_name = 'Административный округ'
        verbose_name_plural = 'Административные округа'

    def __str__(self):
        return self.name


class CultureObject(models.Model):
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
    adm_area = models.ForeignKey(
        AdmArea,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Административный округ',
    )
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Район Москвы',
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
        verbose_name='Статус объекта',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория объекта',
    )
    type = models.ForeignKey(
        TypeObject,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Тип объекта',
    )
    long_position = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        null=True,
        verbose_name='Долгота',
    )
    lat_position = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        null=True,
        verbose_name='Широта',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект культурного наследия'
        verbose_name_plural = 'Объекты культурного наследия'
