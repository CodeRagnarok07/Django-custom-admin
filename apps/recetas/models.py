from ckeditor.fields import RichTextField
from django.db import models
from safedelete.models import HARD_DELETE_NOCASCADE, SafeDeleteModel

# Create your models here.


class Receta(models.Model):
    name = models.CharField(max_length=100, name="nombre")
    photo = models.ImageField(upload_to="recetas/recetas", null=True, blank=True)
    description = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    _safedelete_policy = HARD_DELETE_NOCASCADE

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="recetas/ingredientes")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    _safedelete_policy = HARD_DELETE_NOCASCADE

    def __str__(self):
        return self.name


class CantidadIngerediente(models.Model):
    cantidad = models.FloatField()
    unida = models.CharField(max_length=100, default="gr")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    _safedelete_policy = HARD_DELETE_NOCASCADE
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=True, blank=True)
    ingrediente = models.ForeignKey(
        Ingrediente,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="ingredientes",
    )

    def __str__(self):
        return f"{self.ingrediente.name} - {self.cantidad}"
