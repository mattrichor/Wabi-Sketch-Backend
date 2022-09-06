from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, Sketch, Prompt
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, UserAdmin)
admin.site.register(Sketch)
admin.site.register(Prompt)
