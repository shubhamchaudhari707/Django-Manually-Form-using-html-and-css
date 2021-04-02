from django.contrib import admin
from testapp.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','passward']

admin.site.register(User,UserAdmin)
