from django.contrib import admin
from .models import UserCredential

class CredAdmin(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(UserCredential,CredAdmin)
