from django.contrib import admin
from .models import CompanyAdmin, Verification, Passwordrequest

admin.site.register(CompanyAdmin)
admin.site.register(Verification)
admin.site.register(Passwordrequest)
