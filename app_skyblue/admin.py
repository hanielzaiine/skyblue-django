from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Condominio)
class CondominioAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentoInstitucional)
class DocumentoInstitucionalAdmin(admin.ModelAdmin):
    pass