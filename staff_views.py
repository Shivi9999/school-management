from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import *

@login_required(login_url='/')
def home(request):
    return render(request,'staff/home.html')
@login_required(login_url='/')
def Notification(request):
    staff=Teacher.objects.filter(user=request.user.id)
    for i in staff:
       staff_id=i.id
       notification=Staff_notification.objects.filter(staff_id=staff_id)
       context={'notification':notification}
    return render(request,'staff/notification.html',context)
@login_required(login_url='/')
def mark_as_done(request,status):
    notification=Staff_notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('notification')
@login_required(login_url='/')
def staff_apply_leave(request):
    leave=Teacher.objects.filter(user=request.user.id) 
    for x in leave:
        staff_id=x.id

        staff_leave1=staff_leave.objects.filter(staff_id=staff_id)
     
        context={'staff_leave1':staff_leave1}

    return render(request,'staff/apply_leave.html',context)
@login_required(login_url='/')
def staff_apply_leave_save(request):
    if request.method=="POST":
        date=request.POST.get('date')
        msg=request.POST.get('msg')
        staff=Teacher.objects.get(user=request.user.id)
        save_leave=staff_leave(staff_id=staff,date=date,msg=msg)
        save_leave.save()
        return redirect('staff_apply_leave')
    
@login_required(login_url='/')
def staff_feedback(request):
    leave=Teacher.objects.filter(user=request.user.id)
    print('leavve' ,leave)
    for x in leave:
        staff_id=x.id

        staff_feedback=Staff_Feedback.objects.filter(staff_id=staff_id)
     
        context={'staff_feedback':staff_feedback}
    return render(request,'staff/staff_feedback.html',context)

@login_required(login_url='/')
def staff_feedback_save(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        staff=Teacher.objects.get(user=request.user.id)
        feedback=Staff_Feedback(staff_id=staff,feedback=feedback,feedback_reply="")
        feedback.save()
        return redirect('staff_feedback')




# @login_required(login_url='/')   

# # def take_attendence(request):
#     # context=None
#     # if request.user.user_type == 1:
#     #     classes = Course.objects.all()
#     # else:
#     #     classes = Course.objects.filter(course = request.user.id).all()
#     # context['course'] = "Attendance Management"
#     # context['classes'] = classes
#     # return render(request, 'attendance_class.html',context)
# def take_attendence(request):
#     teacher_id=Teacher.objects.get(admin=request.user.id)
   
#     subject=Subject.objects.filter(teacher=teacher_id)
#     session_year=Session.objects.all()
#     action=request.GET.get('action')
#     get_subject=None
#     get_session_year=None 
#     students=None
#     print('teacher_id',teacher_id)
#     if action is not None:
#         if request.method=="POST":
#             subject_id=request.POST.get("subject_id")
#             session_year_id=request.POST.get("session_year_id")

#             get_subject=Subject.objects.get(id=subject_id)
#             get_session_year=Session.objects.get(id=session_year_id)

#             subject=Subject.objects.filter(id=subject_id)
         
#             for i in subject:
#                 student_id=i.course.id
#                 students=Student.objects.filter(id=student_id)
#     context={'subject':subject,'session_year':session_year,'get_subject':get_subject,'get_session_year':get_session_year,'action':action,'students':students}
#     return render(request,'staff/tack_attendence.html',context)
    
# @login_required(login_url='/')
# def save_attendence(request):
#     if request.method=="POST":
#         subject_id=request.POST.get('subject_id')
#         session_year_id=request.POST.get('session_year_id')
#         attendence_date=request.POST.get('attendence_date')
#         student_id=request.POST.getlist('student_id')
#         get_subject=Subject.objects.get(id=subject_id)
#         get_session_year=Session.objects.get(id=session_year_id)
#         attendence=Attendence(subject_id=get_subject,attendence_date=attendence_date,session_year_id=get_session_year)
#         attendence.save()
#         for i in student_id:
#           stud_id=i
#           int_stud=int(stud_id)
#           p_students=Student.objects.get(id=int_stud)
#           attendence_report=Attendence_report(student_id=p_students,attendence_id=attendence)
#           attendence_report.save()
#     return redirect('take_attendence')

# @login_required(login_url='/')
# def view_attendence(request):
#     teacher_id=Teacher.objects.get(admin=request.user.id)
#     subject=Subjects.objects.filter(teacher_id=teacher_id)
#     session_year=Session.objects.all()
#     action=request.GET.get('action')
#     get_subject=None
#     get_session_year=None 
#     attendence_date=None
#     attendence_report=None
#     if action is not None:
#         if request.method=="POST":
#             subject_id=request.POST.get("subject_id")
#             session_year_id=request.POST.get("session_year_id")
#             attendence_date=request.POST.get("attendence_date")

#             get_subject=Subjects.objects.get(id=subject_id)
#             get_session_year=Session.objects.get(id=session_year_id)
#             attendence=Attendence.objects.filter(subject_id=get_subject,attendence_date=attendence_date)
#             for i in attendence:
#                 attendence_id=i.id
#                 attendence_report=Attendence_report.objects.filter(attendence_id=attendence_id)
#     context={'subject':subject,'session_year':session_year,'action':action,'get_subject':get_subject,'get_session_year':get_session_year,'attendence_date':attendence_date,'attendence_report':attendence_report}
#     return render(request,'staff/view_attendence.html',context)
