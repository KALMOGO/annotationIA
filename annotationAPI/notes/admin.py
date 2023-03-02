from django.contrib import admin
from .models import *

# Register your models here.

class AutoFilter(admin.ModelAdmin):
    list_display = ('id','number','language' ,'creation_date')
    list_filter = ('language',)


class EmotionFilter(admin.ModelAdmin):
    list_display =('id','name', 'emoji', 'creation_date')
    list_filter=('name',)


admin.site.register(Audio, AutoFilter)
admin.site.register(Annotation)
admin.site.register(Emotion, EmotionFilter)