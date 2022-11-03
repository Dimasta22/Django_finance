from django.contrib import admin
from .models import Profit, Expenses, Category

# Register your models here.
admin.site.register(Profit)
admin.site.register(Expenses)
admin.site.register(Category)
