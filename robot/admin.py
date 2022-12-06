from django.contrib import admin
from .models import Value
from .models import Info
from .models import Parameter
from .models import Inventory
# Register your models here.
class dataadmin(admin.ModelAdmin):
    list_display = ('id', 'temp', 'people')
class dataadmin2(admin.ModelAdmin):
    list_display = ('id', 'ear', 'rhand','lhand','mouth')
class dataadmin3(admin.ModelAdmin):
    list_display = ('id', 'sp1', 'ang1', 'dis1','sp2', 'ang2', 'dis2','sp3', 'ang3', 'dis3')
class dataadmin4(admin.ModelAdmin):
    list_display = ('id', 'identify')
    
    
admin.site.register(Inventory,dataadmin4)
admin.site.register(Parameter,dataadmin3)
admin.site.register(Value,dataadmin2)
admin.site.register(Info,dataadmin)


