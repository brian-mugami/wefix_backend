from django.contrib import admin
from .models import UserModel,LocationModel

# Register your models here.
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display =("email", "usertype", "register_date", "phone")
    ordering = ("email",)
    search_fields = ("email",)
    list_max_show_all = True

@admin.register(LocationModel)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_max_show_all = True