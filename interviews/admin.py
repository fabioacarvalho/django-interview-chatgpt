from django.contrib import admin
from .models import *


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('title', 'job', 'completed',)
    list_filter = ('title', 'job', 'completed',)
    search_fields = ('title', 'job', 'completed',)
    inlines = [MessageInline,]



