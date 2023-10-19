from django.contrib import admin
from .models import fun,author,Books,Address,Country


class funAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    list_filter = ("rating","director")
    list_display = ("title","director")


class authorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name")
    list_filter = ("first_name",)

admin.site.register(fun,funAdmin)

# Register your models here.
admin.site.register(author,authorAdmin)
admin.site.register(Books)
admin.site.register(Address)
admin.site.register(Country)