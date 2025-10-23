from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name", "newsletter"]
    # list_display = ["first_name", "last_name",
    # "newsletter", "email", "account"]

    # readonly_fields = ["account"]

    prepopulated_fields = {"slug": ["first_name", "last_name"]}

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "account"
                ]
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": [
                    "newsletter", "slug"
                ],
            },
        ),
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Producttype)
