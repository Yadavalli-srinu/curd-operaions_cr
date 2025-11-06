from django.contrib import admin

from app1.models import employee_model

class employee_admin(admin.ModelAdmin):
    list_display=["name","emp_id","mobile","email","salary","dept","join_date"]
admin.site.register(employee_model,employee_admin)