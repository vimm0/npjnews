from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from apps.news.models import Category, Reporter, Publication, Article


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('title', 'description',)
    list_display = ('title',)


admin.site.register(Reporter)
admin.site.register(Publication)
admin.site.register(Article)
