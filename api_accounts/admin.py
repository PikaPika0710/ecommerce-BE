from django.contrib import admin

from api_accounts.models import Account, Role

admin.site.register(Account)
admin.site.register(Role)