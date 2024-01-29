from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class Ingrediente(models.Model):
    name = models.CharField(max_length=100)
    unida = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="recetas/ingredientes")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)


class CantidadIngerediente(models.Model):
    ingrediente = models.ForeignKey(
        Ingrediente, on_delete=models.CASCADE, null=True, blank=True
    )
    cantidad = models.FloatField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)


class Receta(models.Model):
    name = models.CharField(max_length=100, name="nombre")
    ingredientes = models.ManyToManyField(CantidadIngerediente)
    photo = models.ImageField(upload_to="recetas/recetas", null=True, blank=True)
    description = RichTextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
