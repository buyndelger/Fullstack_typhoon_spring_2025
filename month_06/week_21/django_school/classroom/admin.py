from django.contrib import admin

# Register your models here.
from .models import Profile, Lesson, Reservation

admin.site.register(Profile)
admin.site.register(Lesson)
admin.site.register(Reservation)
