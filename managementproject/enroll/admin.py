from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
admin.site.register(User,UserAdmin)

# Register your models here.
