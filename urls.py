"""School_management_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views,Hod_views,staff_views,student_views,transport_views
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base,name='base'),
    path('', views.Login,name='login'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),
    path('dologout', views.doLogin,name='logout'),
    path('profile', views.profile,name='profile'),
    path('profile/update', views.profile_update,name='profile_update'),
    path('doLogin', views.doLogin,name='doLogin'),
    path('Hod/home', Hod_views.home,name='Hod_home'),
    path('Hod/add_course', Hod_views.add_course,name='add_course'),
    path('Hod/course/view_course', Hod_views.view_course,name='view_course'),
    path('Hod/course/edit/<str:id>', Hod_views.edit_course,name='edit_course'),
    path('Hod/course/delete/<str:id>', Hod_views.delete_course,name='delete_course'),
    path('Hod/course/update', Hod_views.update_course,name='update_course'),
    path('Hod/add_course_save', Hod_views.Add_course_save,name='add_course_save'),
    path('Hod/Teacher/add_teacher', Hod_views.add_teacher,name='add_teacher'),
    path('Hod/Teacher/view_teacher', Hod_views.view_teacher,name='view_teacher'),
    path('Hod/Teacher/delete/<str:user>', Hod_views.delete_teacher,name='delete_teacher'),
    path('Hod/Teacher/edit/<str:id>', Hod_views.edit_teacher,name='edit_teacher'),
    path('Hod/Teacher/update', Hod_views.update_teacher,name='update_teacher'),
    
    path('student/home', student_views.home,name='student_home'),
    path('Hod/Student/add', Hod_views.add_student,name='add_student'),
    path('Hod/Student/view', Hod_views.view_student,name='view_student'),
    path('Hod/Student/edit/<str:id>', Hod_views.edit_student,name='edit_student'),
    path('Hod/Student/update', Hod_views.update_student,name='update_student'),
    path('Hod/Student/delete/<str:user>', Hod_views.delete_student,name='delete_student'),
    path('Hod/Subject/add_subject', Hod_views.add_subject,name='add_subject'),
    path('Hod/Subject/view_subject', Hod_views.view_subject,name='view_subject'),
    path('Hod/Subject/edit/<str:id>', Hod_views.edit_subject,name='edit_subject'),
    path('Hod/Subject/delete/<str:id>', Hod_views.delete_subject,name='delete_subject'),
    path('Hod/Subject/update', Hod_views.update_subject,name='update_subject'),
    path('Hod/add_transport_manager', Hod_views.add_transport_manager,name='add_transport_manager'),
    path('transport_manager/transport_home', transport_views.home,name='transport_home'),
    path('Hod/intimation_letter', Hod_views.intimation_letter,name='intimation_letter'),
    path('Hod/handle_exam', Hod_views.add_exam,name='handle_exam'),
    path('signup_as_a_student', views.signup_as_a_student,name='signup_as_a_student'),
    path('signup_as_a_admin', views.signup_as_a_admin,name='signup_as_a_admin'),
    path('Hod/staff/send_notifications', Hod_views.staff_notifications,name='send_notifications'),
    path('Hod/staff/save_notifications', Hod_views.save_staff_notifications,name='save_staff_notifications'),
    path('Hod/staff/view_leave', Hod_views.staff_view_leave,name='staff_view_leave'),
    path('Hod/staff/approved_leave/<str:id>', Hod_views.approved_leave,name='approved_leave'),
    path('Hod/staff/disapproved_leave/<str:id>', Hod_views.disapproved_leave,name='disapproved_leave'),
    path('Hod/staff/send_staff_feedback', Hod_views.send_staff_feedback,name='send_staff_feedback'),
    path('Hod/staff/save_staff_feedback', Hod_views.save_staff_feedback,name='save_staff_feedback'),
    path('Hod/student/send_student_notification', Hod_views.student_notification,name='send_student_notification'),
    path('Hod/student/save_student_notification', Hod_views.save_student_notification,name='save_student_notification'),
    path('Hod/student/send1_student_feedback', Hod_views.send1_student_feedback,name='send1_student_feedback'),
    path('Hod/student/save1_student_feedback', Hod_views.save1_student_feedback,name='save1_student_feedback'),
    path('Hod/student/view__student_leave', Hod_views.student_view_leave,name='view_student_leave'),
    path('Hod/student/approved_leave/<str:id>', Hod_views.student_approved_leave,name='student_approved_leave'),
    path('Hod/student/disapproved_leave/<str:id>', Hod_views.student_disapproved_leave,name='student_approved_leave'),
   #staff pannel url
    path('staff/home', staff_views.home,name='staff_home'),
    path('staff/notification', staff_views.Notification,name='notification'),
    path('staff/mark_as_done/<str:status>', staff_views.mark_as_done,name='mark_as_done'),
    path('staff/staff_apply_leave', staff_views.staff_apply_leave,name='staff_apply_leave'),
    path('staff/staff_apply_leave_save', staff_views.staff_apply_leave_save,name='staff_apply_leave_save'),
    path('staff/staff_feedback', staff_views.staff_feedback,name='staff_feedback'),
    path('staff/staff_feedback_save', staff_views.staff_feedback_save,name='staff_feedback_save'),
    # path('staff/take_attendence',staff_views.take_attendence,name='take_attendence'),
    # path('staff/save_attendence',staff_views.save_attendence,name='save_attendence'),
    # path('staff/view_attendence',staff_views.view_attendence,name='view_attendence'),
   
   #this is student url 
  
    path('send-notification/', Hod_views.send, name='send-notification'),
    path('firebase-messaging-sw.js',Hod_views.showFirebaseJS,name="show_firebase_js"),
    path('student/home', student_views.home,name='student_home'),
    path('student/notification', student_views.student_noti,name='stud_notification'),
    path('student/student_mark_as_done/<str:status>', student_views.mark_as_done1,name='student_mark_as_done'),
    path('student/student_feedback', student_views.student_feedback,name='student_feedback'),
    path('student/save_student_feedback', student_views.save_student_feedback,name='save_student_feedback'),
  
    path('student/view_book', student_views.view_book,name='view_book'),
    path('student/view_issue_book', student_views.view_issue_book,name='view_issue_book'),
    path('student/fees_submit', student_views.fees_submit,name='fees_submit'),
    path('student/fees_submit_save', student_views.fees_submit_save,name='fees_submit_save'),
    path('student/paytm', student_views.paytm.as_view(),name='paytm'),
    path('student/success', student_views.success,name='success'),
    path('student/paypal', student_views.paypal.as_view(),name='paypal'),
    #path('student/Exam/', student_views.Exam,name='Exam'),
    path('student/question',student_views.student_exam_view, name='question'),
    path('student/question1/<int:id>',student_views.take_exam_view, name='question1'),
    path('student/question2/<int:id>',student_views.start_exam_view, name='question2'),
    path('submit_answer/<int:cat_id>/<int:quest_id>',student_views.submit_answer, name='submit_answer'),
    # path('student/Result', student_views.result,name='Result'),
    # path('student/check_answer/<int:pk>', student_views.check_marks_view,name='check_answer'),
    path('student/student_apply_leave', student_views.student_apply_leave,name='student_apply_leave'),
    path('student/student_apply_leave_save', student_views.student_apply_leave_save,name='student_apply_leave_save'),

    #transport manager pannel
    path('transport_manager/transport_home', transport_views.home,name='transport_home'),
    path('transport_manager/add_bus',transport_views.add_bus,name='add_bus'),
    path('transport_manager/add_driver',transport_views.add_driver,name='add_driver'),
    path('transport_manager/view_bus',transport_views.view_bus,name='view_bus'),
    path('transport_manager/edit_bus/<str:id>',transport_views.edit_bus,name='edit_bus'),
    path('transport_manager/update_bus',transport_views.update_bus,name='update_bus'),
    path('transport_manager/view_driver_transport',transport_views.view_driver_transport,name='view_driver_transport'),
    path('transport_manager/edit_driver/<str:id>',transport_views.edit_driver,name='edit_driver'),
    path('transport_manager/update_driver',transport_views.update_driver,name='update_driver'),
    path('generics/',include('School_management_api.api.urls'),name='generics'),
    path('staff/',include('School_management_api.staff_api.urls'),name='staff'),
    path('student/',include('School_management_api.student_api.urls'),name='student'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

