from django.contrib import admin
from .models import List, Items, Customer

# Register your models here. helps manage models
admin.site.register(List)
admin.site.register(Items)
admin.site.register(Customer)