from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class Coursemodel(admin.ModelAdmin):
   list_display=['user_name','profile_pic']
admin.site.register(AdminHOD)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(Transport_manager)
admin.site.register(Add_bus)
admin.site.register(Add_driver)
admin.site.register(intimation)
admin.site.register(Student_Feedback)
admin.site.register(Student_notification)
admin.site.register(Staff_Feedback)
admin.site.register(student_leave)
admin.site.register(staff_leave)
admin.site.register(Staff_notification)
admin.site.register(Writer_name)
admin.site.register(Book_entry)
admin.site.register(IssuedBook)
admin.site.register(Add_fees)
admin.site.register(Quizequestion)