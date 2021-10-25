from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'data_criacao')
    list_filter = ('usuario', 'data',)

admin.site.register(Evento, EventoAdmin)