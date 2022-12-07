from django.contrib import admin
from api.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qa = User.objects.filter(is_superuser = False)
        if qa:
            return qa
        return False
    fields = ['email','name','phone_number','password']
    list_display = ['id','email','name','phone_number','is_staff','created_date','updated_date']
admin.site.register(User,UserAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display =['id','task_name','user','priority','description','created_date','updated_date']
    fields = ['task_name','user','priority','description']
admin.site.register(Task,TaskAdmin)