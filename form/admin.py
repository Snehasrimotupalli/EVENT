from django.contrib import admin

# Register your models here.
from . models import regForm,Orders


admin.site.register(regForm)

admin.site.register(Orders)
