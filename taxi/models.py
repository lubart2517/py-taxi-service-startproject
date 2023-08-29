from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    country = models.CharField(
        max_length=255,
    )

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    email = models.EmailField()
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.manufacturer.name } {self.model}"
