from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import fun,author,Books,Address,Country,forms_django


class funAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    list_filter = ("rating","director")
    list_display = ("title","director")


class authorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name")
    list_filter = ("first_name",)


class forms_djangoAdmin(admin.ModelAdmin):
    list_display= ("username","email","review")
    list_filter =("username",)
    

admin.site.register(fun,funAdmin)

# Register your models here.
admin.site.register(author,authorAdmin)
admin.site.register(Books)
admin.site.register(Address)
admin.site.register(Country)
admin.site.register(forms_django,forms_djangoAdmin)