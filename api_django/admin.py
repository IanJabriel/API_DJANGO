from django.contrib import admin
from .models import User, Course, Area, Organization

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Area)
admin.site.register(Organization)