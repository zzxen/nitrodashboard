from django.contrib import admin
from .models import CryptoCurrency , Notes , Updates , New , Service

# Register your models here.

admin.site.register(CryptoCurrency)
admin.site.register(Notes)
admin.site.register(Updates)
admin.site.register(New)
admin.site.register(Service)