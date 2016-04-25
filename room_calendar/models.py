from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

class OfficeLocation(models.Model):
    office_abbreviation = models.CharField(max_length=5)
    office_city = models.CharField(max_length=200)
    office_address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.office_city

class Room(models.Model):
    # This is the short name of the room that matches the exchange connector filename
    room_name_short = models.CharField(max_length=200)
    room_name_long = models.CharField(max_length=200)
    room_location = models.ForeignKey(OfficeLocation, on_delete=models.CASCADE)
    room_mailbox = models.CharField(max_length=200)
    
    def __str__(self):
        return self.room_location + self.room_name_long

class Reservation(models.Model):
    # This is the exchange ID provided via PyExchange
    reservation_id = models.CharField(max_length=500)
    reservation_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation_title = models.CharField(max_length=200)
    # This is required by Exchange, but will only include the room's inbox
    reservation_attendees = models.CharField(max_length=200)
    reservation_start = models.DateTimeField(default=timezone.now())
    reservation_end = models.DateTimeField(default=timezone.now()
        + datetime.timedelta(minutes=15))
    reservation_owner = models.CharField(max_length=200)
    
    def __str__(self):
        title = "Title: " + self.reservation_title
        location = "\nLocation: " + self.reservation_room
        owner = "\nOwner: " + self.reservation_owner
        time = "\nStart/End: " + self.reservation_start + " - " + self.reservation_end
        return title + location + owner + time