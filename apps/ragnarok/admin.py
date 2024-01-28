from django.contrib import admin

from .models import CantidadIngerediente, Ingrediente, Receta

# Register your models here.


admin.site.register(CantidadIngerediente)
admin.site.register(Ingrediente)
admin.site.register(Receta)
