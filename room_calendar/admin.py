from django.contrib import admin

from django.contrib import admin

from .models import Room, OfficeLocation

class RoomInline(admin.TabularInline):
    fields = ['room_name_long', 'room_name_short', 'room_mailbox']
    model = Room
    extra = 1

class OfficeLocationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Address Information', {'fields': ['office_address', 'office_city']}),
        ('Other Information', {'fields': ['office_abbreviation']}),
    ]
    
    inlines = [RoomInline]
admin.site.register(OfficeLocation, OfficeLocationAdmin)