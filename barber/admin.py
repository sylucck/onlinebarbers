from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Barber)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(About, AboutAdmin)
