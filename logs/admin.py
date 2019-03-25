from django.contrib import admin
from .models import Topic, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "topic")


# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
