from django.contrib import admin

from .models import Plan
from .models import Customer

admin.site.register(Plan)
admin.site.register(Customer)
# Register your models here.
