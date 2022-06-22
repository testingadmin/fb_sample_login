from django.contrib import admin
from facebookpage.models import UserPerson


@admin.register(UserPerson)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password']

