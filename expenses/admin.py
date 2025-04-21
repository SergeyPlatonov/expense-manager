from django.contrib import admin
from .models import Expense

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "amount", "date", "user")
    list_filter = ("category", "date", "user")
    search_fields = ("title", "category", "user__username")

# admin.site.register(Expense, ExpenseAdmin)

