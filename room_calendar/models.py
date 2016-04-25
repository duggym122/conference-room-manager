from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

class Room(models.Model):
    room_location = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.room_location + ", " + self.room_name

class Reservation(models.Model):
    reservation_title = models.CharField(max_length=200)
    reserved_room_location = models.CharField(max_length=200)
    reserved_room_name = models.CharField(max_length=200)
    reserved_by = models.CharField(max_length=200)
    reserved_on_date = models.DateTimeField('date published')
    reservation_start = models.DateTimeField('date published')
    reservation_end = models.DateTimeField('date published')
    reservation_exchange_id = models.CharField(max_length=200)
    
    def __str__(self):
        title = self.reservation_title
        location = "\n Room: " + self.reserved_room_location + ", " + self.reserved_room_name
        owner = "\n Reserved By: " + self.reserved_by + "\n Reserved On: " + self.reserved_on_date
        timing = "\n Start/End: " + self.reservation_start + " - " + self.reservation_end
        return title + location + timing + owner