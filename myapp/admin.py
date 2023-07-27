from django.contrib import admin
# Register your models here.
from .models import expense
# admin.site.register(expense)
@admin.register(expense)
class ExpenseAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'value', 'description', 'category', 'date', 'created_at', 'updated_at', 'created_by')
