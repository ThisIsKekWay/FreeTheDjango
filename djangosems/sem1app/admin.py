from django.contrib import admin
from .models import Client, Order, Product
from django.utils.html import format_html


@admin.action(description='Удалить изображение')
def reset_image(modeladmin, request, queryset):
    queryset.update(image='products/default.jpg')


class ProductAdmin(admin.ModelAdmin):

    @staticmethod
    def show_image(obj):
        return format_html('<img src="{}" style="max-height: 300px; max-width: 300px" />'.format(obj.image.url))

    list_display = ['show_image', 'name', 'description', 'price', 'quantity', 'updated']
    ordering = ['-updated']
    list_filter = ['updated']
    search_fields = ['name']
    search_help_text = 'Enter product name'
    actions = [reset_image]

    readonly_fields = ['updated', 'image_preview']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его описание',
                'fields': ['description', 'image_preview'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'Прочее',
            {
                'description': 'Дата обновления',
                'fields': ['updated'],
            }
        )
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'product_id', 'total_price', 'order_date']
    ordering = ['-order_date']
    list_filter = ['order_date', 'client_id']
    readonly_fields = ['order_date', 'total_price', 'client', 'product']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client']
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его описание',
                'fields': ['product', 'total_price', 'order_date'],
            }
        )
    ]


class AdminUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone_num', 'reg_date']
    readonly_fields = ['reg_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'fields': ['address', 'phone_num', 'reg_date'],
            }
        )
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, AdminUser)
