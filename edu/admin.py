from django.contrib import admin

# Register your models here.
from .models import Teachers, Grades, Students, Subjects

admin.site.register(Teachers)
admin.site.register(Grades)
admin.site.register(Students)
admin.site.register(Subjects)





