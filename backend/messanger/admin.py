from django.contrib import admin
from .models import MessageFromSpace


@admin.register(MessageFromSpace)
class MessageFromSpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'read', 'text')
