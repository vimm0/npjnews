from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from apps.news.models import News, Category, Reporter, Publication


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title',)
@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Reporter)
admin.site.register(Publication)
admin.site.register(News)
