# conference-room-manager

## Project Information
| Package       | Description   | Version|
| ------------- |:-------------:| -----:|
| conference-room-manager| Django application to manage conference rooms and their reservations at multiple office locations | Pre-Release |

## Overview
The Conference Room Manager will allow administrative users to update available office locations, conference rooms tagged to those locations, and any reservations made against those rooms. Via the public-facing part of the application, users will be able to view the availability for a certain room, request access to that room on the fly (in addition to using their existing Exchange system to reserve the room), and see suggestions of other open rooms. 

**NOTE: This project is still in very early development, so it is subject to some very drastic, and potentially backwards-incompatible changes during the process.**

## Installation

### Django

For information on how to install Django, see their documentation. Version 1.9 as of the time of this writing: https://docs.djangoproject.com/en/1.9/intro/install/

#### Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

### PyExchange

This project uses PyExchange to manage room reservations via Exchange. It is required to interface with Exchange systems and, per their documentation, is only directly tested/developed against Exchange 2010. Their full documentation can be found here: https://pyexchange.readthedocs.org/en/latest 

In order to install, follow their provided directions: http://pyexchange.readthedocs.org/en/latest/#installation 

## Running conference-room-manager

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT

## GNU Affero General Public License v3.0

The Conference Room Manager will allow users to manage office locations, conference rooms, and reservations.
Copyright (C) 2016  Douglas Melvin

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.