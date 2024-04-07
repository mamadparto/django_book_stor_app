from django.contrib import admin
from .models import Book, comment


class commentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'datetime_created')


admin.site.register(Book)
admin.site.register(comment, commentAdmin)
