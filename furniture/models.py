from tabnanny import check
from django.db import models

class Color(models.Model):
    """Продукт"""
    title = models.CharField("Название", max_length=100)
    photo = models.ImageField("Фото",  upload_to="colored/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

class Group(models.Model):
    """Группа"""
    title = models.CharField("Название", max_length=100)
    photo = models.ImageField("Фото",  upload_to="products/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

class Artikle(models.Model):
    """Артикл"""
    title = models.CharField("Название", max_length=100)
    artikle = models.CharField("Артикул", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Автикл"
        verbose_name_plural = "Артиклы"

class Product(models.Model):
    """Продукт"""
    title = models.CharField("Название", max_length=100)
    artikle = models.ForeignKey(Artikle, verbose_name="Артикул", on_delete=models.CASCADE)
    width = models.PositiveIntegerField("Ширина")
    height = models.PositiveIntegerField("Высота")
    depth = models.PositiveIntegerField("Глубина")
    coast = models.PositiveIntegerField("Цена")
    colors = models.ManyToManyField(Color, verbose_name="Основной цвет")
    ffrancia = models.PositiveIntegerField("Гарантия")
    photo = models.ImageField("Фото",  upload_to="products/")
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"

class Order(models.Model):
    """Артикл"""
    user = models.CharField("Пользователь", max_length=100)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField("Количество")
    phone = models.CharField("Телефон", max_length=30)
    check_order = models.BooleanField("Обработан", default=False)

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"




