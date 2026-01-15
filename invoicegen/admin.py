from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'invoice_number', 'client_name', 'client_city', 'client_country', 'amount', 'paid', 'created_at']
    list_filter = ['paid', 'created_at']
    search_fields = ['title', 'invoice_number']
    ordering = ['-created_at']
    fieldsets = (
        ('Invoice Info', {
            'fields': ('title', 'invoice_number', 'amount', 'paid')
        }),
        ('Client (Bill To)', {
            'fields': (
                'client_name',
                'client_address',
                'client_city',
                'client_country',
            )
        }),
    )