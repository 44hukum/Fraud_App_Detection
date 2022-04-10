from pickle import NONE
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usermanagement.models import CustomUser

class CustomUerAdmin(UserAdmin):
    list_display =(
        'username','email','first_name','last_name','phonenumber'
    )
    fieldsets =(
        ('Required Fields',{
            'fields':('username','password')
        }),
        ('Personal info',{  
            'fields':(
                'first_name','last_name','email','phonenumber'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )
    add_fieldsets = (
        ('Registration',{
            'fields':('username','password1','password2')
        }),
        ('Personal info',{
            'fields':(
                'first_name',
                'last_name',
                'email',
                'phonenumber'
            )
        })
    )

admin.site.register(CustomUser,CustomUerAdmin)