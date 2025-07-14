from django.contrib import admin
from .models import Expense

# Registering the Expense model in the admin panel
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'category', 'date', 'user']
    list_filter = ['category', 'date']
    search_fields = ['title', 'note']
