from django.contrib import admin

from TransferApp.models import Customer, Transaction


admin.site.register(Customer)
admin.site.register(Transaction)

# Register your models here.
