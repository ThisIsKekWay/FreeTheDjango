from django.contrib import admin
from .models import Category, Product


@admin.action(description='Reset quantity to 0')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'price', 'quantity', 'date_added', 'rating']
    ordering = ['-quantity', 'category']
    list_filter = ['category', 'date_added']
    search_fields = ['name']
    search_help_text = 'Enter product name'
    actions = [reset_quantity]

    # feilds = ['name', 'category', 'description', 'price', 'quantity', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
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
                'fields': ['description', 'category'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг формируется автоматически на основе отзывов покупателей',
                'fields': ['rating', 'date_added'],
            }
        )
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

