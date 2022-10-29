from django.db import models
from django.utils import timezone
from django.db.models import TextChoices



class CategoryChoices(TextChoices):
    ELECTRONICS = 'Electronics', 'Электроника'
    KITCHEN_ELECTRONICS = 'Kitchen_electronics', 'Кухонная электроника'
    CARS = 'Cars', 'Машины'
    OTHER = 'Other', 'Разное'


class Product(models.Model):
    name = models.CharField(
        verbose_name='Продукт',
        max_length=50,
        null=False,
        blank=False
    )
    category = models.CharField(
        verbose_name="Категория",
        choices=CategoryChoices.choices,
        max_length=50,
        null=False,
        blank=False)
    description = models.TextField(
        verbose_name='Описание',
        max_length=2000,
        null=False,
        blank=False
    )
    image = models.ImageField(
        verbose_name='Картинка',
        default='default_image.png',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True)
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        default=False,
        null=False
    )

    def __str__(self):
        return f"{self.name} - {self.category}- {self.description}"



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

