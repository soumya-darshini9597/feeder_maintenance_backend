from django.contrib import admin
from .models import *

@admin.register(Feeder)
class feeder(admin.ModelAdmin):
    list_display = ('id','mesuredHeight','stepCount','conformationHeight')
