from django.contrib import admin

from .models import CantidadIngerediente, Ingrediente, Receta

# Register your models here.


class IngredienteTableAdmin(admin.ModelAdmin):
    model = Ingrediente
    list_display_links = ["id"]
    list_display = [
        "id",
        "name",
    ]
    list_editable = [
        "name",
    ]


admin.site.register(Ingrediente, IngredienteTableAdmin)


class CantidadesInline(admin.TabularInline):
    model = CantidadIngerediente
    extra = 1


# class ingredienteCantidadAdmin(admin.ModelAdmin):
#     list_display_links = ["id"]
#     list_display = ["codigo", "id", "cantidad"]

#     # list_editable = ["name"]

#     @admin.display(description="codigo")
#     def codigo(self, obj):
#         return obj.id


# admin.site.register(CantidadIngerediente, ingredienteCantidadAdmin)


class RecetaAdmin(admin.ModelAdmin):
    list_display_links = ["codigo"]
    list_display = ["codigo", "nombre"]
    inlines = [CantidadesInline]

    # list_editable = ["name"]
    @admin.display(description="codigo")
    def codigo(self, obj):
        print(obj.__dict__)
        return obj.id

    # @admin.display(description="ingredientes")
    # def codigo(self, obj):
    #     return obj.ingredientes


admin.site.register(Receta, RecetaAdmin)
