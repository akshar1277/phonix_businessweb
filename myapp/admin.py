from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Contact,Positions
# Register your models here.

class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','first_name','last_name','company','email','phone','interested_in','estimated_budget','project_timeline','about_us','description']

class PositionsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','name','email','phone','portfolio_url']


admin.site.register(Contact,ContactAdmin)  
admin.site.register(Positions,PositionsAdmin)      