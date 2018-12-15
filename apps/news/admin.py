from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from apps.news.models import Category, Reporter, Publication, Article


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('title', 'slug', 'description',)
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Reporter)
# admin.site.register(Publication)
admin.site.register(Article)
