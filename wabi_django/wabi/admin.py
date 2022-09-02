from django.contrib import admin
from .models import User, Sketch, Prompt
# Register your models here.

admin.site.register(User)
admin.site.register(Sketch)
admin.site.register(Prompt)
