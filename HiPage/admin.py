from django.contrib import admin
from HiPage.models import Good, Size, Type, Good_Get

class GoodAdmin(admin.ModelAdmin):
    model = Good
    list_display = ('Name', 'Available')
    list_filter = ['id']
    search_fields = ['Name']
    fieldsets = [
    ('Name', {'fields': ['Name']}),
    ('Type', {'fields': ['Type']}),
    ('Available', {'fields': ['Available']}),
    ('Photo', {'fields': ['Photo'], 'classes': ['collapse']}),
    ('Discount', {'fields': ['Discount'], 'classes': ['collapse']}),
    ('Price', {'fields': ['Price']}),
    ('Sizes', {'fields': ['Size']}),
    ('URL', {'fields': ['URL']}),
    ]


admin.site.register(Good, GoodAdmin)
admin.site.register(Size)
admin.site.register(Type)
admin.site.register(Good_Get)
