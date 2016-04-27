from django.contrib import admin

from django.contrib import admin

from .models import Room, OfficeLocation, Reservation

class RoomInline(admin.TabularInline):
    fields = ['room_name_long', 'room_name_short', 'room_mailbox']
    model = Room
    extra = 1

class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meeting Information',{'fields' : ['reservation_title','reservation_room']}),
        ('Meeting Attendees',{'fields' : ['reservation_owner','reservation_attendees']}),
        ('Meeting Duration',{'fields' : ['reservation_start','reservation_end']}),
        ('Exchange Data',{'fields' : ['reservation_id']}),
    ]
admin.site.register(Reservation, ReservationAdmin)

class OfficeLocationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Address Information', {'fields': ['office_address', 'office_city']}),
        ('Other Information', {'fields': ['office_abbreviation']}),
    ]
    
    inlines = [RoomInline]
admin.site.register(OfficeLocation, OfficeLocationAdmin)