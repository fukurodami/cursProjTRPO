from django.contrib import admin
from .models import Color, Artikle, Product, Group, Order

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
#     list_filter = ('status', 'created', 'publish', 'author')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'publish'
#     ordering = ['status', 'publish']

admin.site.register(Color)
admin.site.register(Artikle)
admin.site.register(Product)
admin.site.register(Group)
admin.site.register(Order)