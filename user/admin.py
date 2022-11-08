from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Account_Information

admin.site.register(User, UserAdmin)
admin.site.register (Account_Information)
# admin.site.register (UserRegister)
# Register your models here.
