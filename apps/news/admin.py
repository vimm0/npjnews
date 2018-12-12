from django.contrib import admin

from apps.news.models import News


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title',)


admin.site.register(News)
