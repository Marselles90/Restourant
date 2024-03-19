from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Table)
admin.site.register(BookTable)
admin.site.register(Event)
admin.site.register(Response)
