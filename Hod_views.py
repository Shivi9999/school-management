from django.shortcuts import render,redirect
from app.models import *
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from django.shortcuts import render,HttpResponse
import requests
import json

# Create your views here.

def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAAam0Fww4:APA91bEa44  2qCtF-BVe0qWdB7li6Wu5m6-PqobuGLf_bc6sOZTWfCTWaZL8d_qnKX3_f-TGnAndc6ARfQ43XHiMoceo-MFTWwcrZpWuhAx2nOWXiNJV4jS_bh7xXbYki4gJvsEXnjk"
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}
    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            # "image" : "https://"Users\Simran\Pictures\nature.jpg",
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }
    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())
def send(request):
    registration  = ['eAepkaMCQomvOlBtm6PzCM:APA91bFGrD06SKCDYsnaqJqfGP49juf5i2SKEtGrGoBoXPQ10A5Y7d3XljCi2jc7at3mepFa881pqtHFCoZe68w1Ec6dnXOKiuuGFVYKNYwSyfqOzu1hxy1lWTEhMV4-sgBzHxvhle-R'
]
    send_notification(registration , 'hello this is shivani from cyber impulse solutions ' , 'notification alert')
    return HttpResponse("sent")
def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/9.17.0/firebase-app.js")'\
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js")'\
        'var firebaseConfig = {'\
           ' apiKey: "AIzaSyDyPocj-7kA9CKYeVSwG5KM2N_5_rwZWk0",'\
            'authDomain: "schhol-d8553.firebaseapp.com",'\
            'databaseURL: "https://schhol-d8553.firebaseio.com",'\
            'projectId: "schhol-d8553",'\
            'storageBucket: "schhol-d8553.appspot.com",'\
            'messagingSenderId: "778917612722",'\
            'appId: "1:778917612722:web:90c989b3d2f79d414b4dab",'\
            'measurementId: "G-JDW4RFR844"'\
       '};'\
        'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
            '    console.log(payload);' \
            '    const notification=JSON.parse(payload);' \
            '    const notificationOption={' \
            '        body:notification.body,' \
            '        icon:notification.icon' \
            '    };' \
            '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
            '});'

    return HttpResponse(data,content_type="text/javascript")

# cred = credentials.Certificate('static/school_firebase.json')
# firebase_admin.initialize_app(cred, name='School090909')

# def send_fcm_notification(device_token, title, message):
#     # Create the message
#     fcm_message = messaging.Message(
#         notification=messaging.Notification(
#             title=title,
#             body=message
#         ),
#         token=device_token
#     )

#     # Send the message
#     response = messaging.send(fcm_message)
#     return response

# # Usage example
# device_token = 'fFOPebjiRGSCsSPkv73Nph:APA91bEkQklqjzGG-0xYGOrHZ9K_J89bbN5Wx94KtQvNxLUDu1wUfP0TZpiTwLw-wrJ3TkuwGIQQGWUe0IM1ECRbG0LAFL0P8psGssHKitW9kFG01AUhYCOMcHwB8qqxe0Ettcl4Bp7K'  # Replace with the actual device token
# notification_title = 'Notification Title'
# notification_message = 'Notification Message'

# response = send_fcm_notification(device_token, notification_title, notification_message)
# print('Notification sent:', response)
def home(request):
    student_count=Student.objects.all().count()
    staff_count=Teacher.objects.all().count()
    course_count=Course.objects.all().count()
    subject_count=Subjects.objects.all().count()
    student_gender_male=Student.objects.filter(Gender='Male').count()
    print('male',student_gender_male)
    student_gender_female=Student.objects.filter(Gender='Female').count()
    print('female',student_gender_female)
    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
        }
    
    return render(request, 'Hod/home.html',context)
def add_course(request):
    return render(request, "Hod/add_course.html")
def Add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        course_id = request.POST.get('course')
        try:
            course_model = Course(course_id=course_id)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')
 
def view_course(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'Hod/view_course.html', context)
 
 
def edit_course(request, id):
    courses = Course.objects.get(id=id)
    context = {
        "courses": courses,
        "id": id
    }
    return render(request,'Hod/edit_course.html',context)
 
 
def update_course(request):
    if request.method=="POST":
      course=request.POST.get('course')
      course_id=request.POST.get('course_id')
      course1=Course.objects.get(id=course_id)
      course1.course=course
      course1.save()
      messages.success(request,'Data Updated succssefully')  
      return redirect('view_course')
    return render(request,'Hod/edit_course.html')
def delete_course(request, id):
    course1 = Course.objects.get(id=id)
    course1.delete()
    messages.success(request,'Data deleted')  
    return redirect('view_course')   
def add_teacher(request): 
    if request.method == "POST":
            profile_pic=request.FILES.get('profile_pic')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            user_name=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            gender=request.POST.get('Gender')
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email is already exist')
                return redirect('add_teacher')
            elif User.objects.filter(user_name=user_name).exists():
                messages.error(request,'username is already exist')
                return redirect('add_teacher')
            else:
                user = User(profile_pic=profile_pic,first_name=first_name,last_name=last_name,user_name=user_name,email=email,user_type=2)
                user.set_password(password)
                user.save()
                teacher=Teacher(
                user=user,
                
                address=address,
                gender=gender
                )
                teacher.save()
                messages.success(request,'Data is Submitted')
                return redirect('view_teacher')
    
    return render(request,'Hod/add_teacher.html')
@login_required(login_url='/')
def view_teacher(request):
    teacher=Teacher.objects.all()
    context={'teacher':teacher}
    return render(request,'Hod/view_teacher.html',context)
@login_required(login_url='/')
def edit_teacher(request,id):
    teacher=Teacher.objects.filter(id=id)
    
    context={'teacher':teacher}
    return render(request,'Hod/edit_teacher.html',context)
@login_required(login_url='/')
def update_teacher(request):
    staff_id=request.POST.get('staff_id')
    if request.method=="POST":
            
            profile_pic=request.FILES.get('profile_pic')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            Gender=request.POST.get('Gender')
            user=User.objects.get(id=staff_id)
            user.first_name=request.POST.get('first_name')
            user.last_name=request.POST.get('last_name')
            user.username=request.POST.get('username')
            user.email=request.POST.get('email')
            if password!=None and password!="":
                user.set_password(password)
                if profile_pic!=None and profile_pic!="":
                    user.profile_pic=profile_pic 
            user.save()
            teacher=Teacher.objects.get(user=staff_id)
            teacher.address=address
            teacher.Gender=Gender
            teacher.save()
            messages.success(request,'Data updated succseffuly')  
            return redirect('view_teacher')
    return render(request,'Hod/edit_teacher.html')
@login_required(login_url='/')   
def delete_teacher(request,user): 
    teacher = User.objects.get(id=user)
    teacher.delete()
    messages.success(request,'Data deleted')  
    return redirect('view_teacher')   
@login_required(login_url='/')
def add_student(request):
    course=Course.objects.all()
    
    if request.method=="POST":
       profile_pic=request.FILES.get('profile_pic')
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       email=request.POST.get('email')
       user_name=request.POST.get('username')
       password=request.POST.get('password')
       address=request.POST.get('address')
       course_id=request.POST.get('course_id')
      
       Gender=request.POST.get('Gender')
       if User.objects.filter(email=email).exists():
           messages.error(request,'Email is already exist')
           return redirect('add_student')
       elif User.objects.filter(user_name=user_name).exists():
           messages.error(request,'username is already exist')
           return redirect('add_student')
       else:
           user=User(first_name=first_name,last_name=last_name,email=email,user_name=user_name,profile_pic=profile_pic, user_type=3)
           user.set_password(password)
           user.save()
           course=Course.objects.get(id=course_id)
          
           student=Student(
               user=user,
              
               address=address,
              
               course_id=course,
               Gender=Gender
           )
           student.save()
           messages.success(request,'Data is saved successfully!')
           return redirect('view_student')
    context={'course':course}
    return render(request,'Hod/add_student.html',context)
@login_required(login_url='/')
def view_student(request):
    student=Student.objects.all()
    context={'student':student}
    return render(request,'Hod/view_student.html',context)
@login_required(login_url='/')
def edit_student(request,id):
    student=Student.objects.filter(id=id)
    course=Course.objects.all()
    
    context={'student':student,'course':course}
    return render(request,'Hod/edit_student.html',context)
@login_required(login_url='/')
def update_student(request):
    
    if request.method=="POST":
        student_id=request.POST.get('student_id')
      
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        Gender=request.POST.get('Gender')
        course_id=request.POST.get('course_id')
      
        user=User.objects.get(id=student_id)
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        if password!=None and password!="":
            user.set_password(password)
            if profile_pic!=None and profile_pic!="":
                user.profile_pic=profile_pic 
        user.save()
        student=Student.objects.get(user=student_id)
        student.address=address
        student.Gender=Gender
        course=Course.objects.get(id=course_id)
        student.course_id=course
        
      
        student.save()
        messages.success(request,'Data succssefully updated')
        return redirect('view_student')
    return render(request,'Hod/edit_student.html')
@login_required(login_url='/')
def delete_student(request,user): 
    student = User.objects.get(id = user)
    student.delete()
    messages.success(request,'Data deleted')  
    return redirect('view_student')  
def add_subject(request): 
    course2=Course.objects.all()
    teacher1=Teacher.objects.all()
    if request.method=="POST":
        subject_name=request.POST.get('subject_name')
        course_id=request.POST.get('course_id')
        staff_id=request.POST.get('staff_id')
        course=Course.objects.get(id=course_id)
        teacher=Teacher.objects.get(id=staff_id)
        user=Subjects(subject_name=subject_name,course=course,teacher=teacher)
        user.save()
        messages.success(request,'Data added succseffuly')  
        return redirect('add_subject')
    context={'teacher1':teacher1,'course2':course2}
    
    return render(request,'Hod/add_subject.html',context)
@login_required(login_url='/')
def view_subject(request):
    subject=Subjects.objects.all()
    context={'subject':subject}
    return render(request,'Hod/view_subject.html',context)
@login_required(login_url='/')
def edit_subject(request,id):
    subject=Subjects.objects.get(id=id)
    course=Course.objects.all()
    teacher=Teacher.objects.all()
    context={'subject':subject,'course':course,'teacher':teacher}
    return render(request,'Hod/edit_subject.html',context)
@login_required(login_url='/')
def update_subject(request):  
    if request.method=="POST":
       subject_id=request.POST.get('subject_id')
       subject_name=request.POST.get('subject_name')
       course_id=request.POST.get('course_id')
       staff_id=request.POST.get('staff_id')

       course=Course.objects.get(id= course_id)
       teacher=Teacher.objects.get(id=staff_id)
       subject=Subjects(id=subject_id,course=course,teacher=teacher,subject_name=subject_name)
       subject.save()
       messages.success(request,'Data Updated succssefully')  
       return redirect('view_subject')
    return render(request,'Hod/edit_subject.html')
@login_required(login_url='/')
def delete_subject(request,id): 
    subject = Subjects.objects.get(id =id)
    subject.delete()
    messages.success(request,'Data deleted')  
    return redirect('view_subject')   
def add_transport_manager(request):
    if request.method=="POST":
       profile_pic=request.FILES.get('profile_pic')
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       email=request.POST.get('email')
       user_name=request.POST.get('username')
       password=request.POST.get('password')
       address=request.POST.get('address')
     
       
       Gender=request.POST.get('Gender')
       if User.objects.filter(email=email).exists():
           messages.error(request,'Email is already exist')
           return redirect('add_transport_manager')
       elif User.objects.filter(user_name=user_name).exists():
           messages.error(request,'username is already exist')
           return redirect('add_transport_manager')
       else:
           user=User(first_name=first_name,last_name=last_name,email=email,user_name=user_name,profile_pic=profile_pic, user_type=4)
           user.set_password(password)
           user.save()
          
           manager=Transport_manager(
               user=user,
               address=address,
              
               Gender=Gender
           )
           manager.save()
           messages.success(request,'Data is saved successfully!')
           return redirect('add_transport_manager')
    
   
    return render(request,'Hod/transport_manager.html')
def View_buses(request):
    bus=Add_bus.objects.all()
    context={"bus":bus}
    return render(request,'Hod/view_buses.html',context)
def view_drivers(request):
    drivers=Add_driver.objects.all()
    context={'drivers':drivers}
    return render(request,'Hod/view_drivers.html',context)
def delete_drivers(request,id):
    drivers=Add_driver.objects.get(id=id)
    drivers.delete()
    messages.success(request,'Data deleted')  
    return redirect('view_drivers')
def intimation_letter(request):
   if request.method=="POST":
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = 'b97ciss@gmail.com'
        email=request.POST.get('email','')
        c=intimation(subject=subject,message=message,email=email)
        c.save()
        messages.success(request,'Message send to your mailbox')
        if subject and message and from_email:
            try:
                c=send_mail(subject, message, from_email, [email])
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            return redirect('intimation_letter')
        
            # In reality we'd use a form class
            # to get proper validation errors.
   return render(request,'Hod/intimation_letter.html')    
def add_exam(request):
    course=Course.objects.all()
    subject=Subjects.objects.all()
    if request.method=="POST":
        category=request.POST.get('course')
        question=request.POST.get('question')
        option1=request.POST.get('option1')
        option2=request.POST.get('option2')
        option3=request.POST.get('option3')
        option4=request.POST.get('option4')
        level=request.POST.get('level')
        time_limit=request.POST.get('time_limit')
        right_opt=request.POST.get('right_opt')
        course1=Course.objects.get(id=category)
       
        c=Quizequestion(category=course1,question=question,option1=option1,option2=option2,option3=option3,option4=option4,
                   level=level,time_limit=time_limit,right_opt=right_opt)
        c.save()
        return redirect('handle_exam')
    context={'course':course,'subject':subject}
    return render(request,'Hod/quize_category.html',context)
def staff_notifications(request):
    staff=Teacher.objects.all()
    see_notification=Staff_notification.objects.all().order_by('-id')
    
    # device_token = 'fFOPebjiRGSCsSPkv73Nph:APA91bEkQklqjzGG-0xYGOrHZ9K_J89bbN5Wx94KtQvNxLUDu1wUfP0TZpiTwLw-wrJ3TkuwGIQQGWUe0IM1ECRbG0LAFL0P8psGssHKitW9kFG01AUhYCOMcHwB8qqxe0Ettcl4Bp7K'  # The FCM device token of the user you want to send the notification to
    # title = 'Notification Title'
    # message = 'Notification message body'
    # send_fcm_notification(device_token, title, message)
    context={"staff":staff,'see_notification':see_notification}

    return render(request,'Hod/staff_notifications.html',context)
@login_required(login_url='/')  
def save_staff_notifications(request):
    if request.method=="POST":
        staff_id=request.POST.get('staff_id')
        message=request.POST.get('message')
        staff=Teacher.objects.get(user=staff_id)
        notification=Staff_notification(staff_id=staff,message=message)
        
        # device_token = 'fFOPebjiRGSCsSPkv73Nph:APA91bEkQklqjzGG-0xYGOrHZ9K_J89bbN5Wx94KtQvNxLUDu1wUfP0TZpiTwLw-wrJ3TkuwGIQQGWUe0IM1ECRbG0LAFL0P8psGssHKitW9kFG01AUhYCOMcHwB8qqxe0Ettcl4Bp7K'  # The FCM device token of the user you want to send the notification to
        # title = 'Hello shivani'
        # message = 'Notification message body'
        # send_fcm_notification(device_token, title, message)
        notification.save()
        return redirect('send_notifications')
@login_required(login_url='/')  
def staff_view_leave(request):
    leave_v=staff_leave.objects.all()
    teacher=Teacher.objects.all()
    context={'leave_v':leave_v,'teacher':teacher}
    return render(request,'Hod/staff_leave.html',context)
@login_required(login_url='/')  
def approved_leave(request,id):
    status=staff_leave.objects.get(id=id)
    status.status=1
    status.save()
    return redirect('staff_view_leave')
    
@login_required(login_url='/')      
def disapproved_leave(request,id):
    status=staff_leave.objects.get(id=id)
    status.status=2
    status.save()
    return redirect('staff_view_leave')

def student_view_leave(request):
    leave_v=student_leave.objects.all()
    student=Student.objects.all()
    context={'leave_v':leave_v,'student':student}
    return render(request,'Hod/student_leave.html',context)
@login_required(login_url='/')  
def student_approved_leave(request,id):
    status=student_leave.objects.get(id=id)
    status.status=1
    status.save()
    return redirect('view_student_leave')
    
@login_required(login_url='/')      
def student_disapproved_leave(request,id):
    status=student_leave.objects.get(id=id)
    status.status=2
    status.save()
    return redirect('view_student_leave')


def send_staff_feedback(request):
   
    feedback=Staff_Feedback.objects.all()
    context={'feedback':feedback}
    return render(request,'Hod/staff_feedback1.html',context)

def save_staff_feedback(request):
    if request.method=="POST":
       feedback_id=request.POST.get('feedback_id')
       feedback_reply=request.POST.get("feedback_reply")

       feedback=Staff_Feedback.objects.get(id=feedback_id)
       feedback.feedback_reply=feedback_reply
       feedback.status=1
       feedback.save()
       return redirect('send_staff_feedback')
    
def student_notification(request):
     student=Student.objects.all()
     student_noti=Student_notification.objects.all()
     context={"student":student,'student_noti':student_noti}
     return render(request,'Hod/student_notification.html',context)


def save_student_notification(request):
    if request.method=="POST":
        student_id=request.POST.get('student_id')
        message=request.POST.get('message')
        student=Student.objects.get(user=student_id)
        notification=Student_notification(student_id=student,message=message)
        notification.save()
        return redirect('send_student_notification')
def send1_student_feedback(request):
   
    feedback1=Student_Feedback.objects.all()
    context={'feedback1':feedback1}
    return render(request,'Hod/student_feedback1.html',context)

def save1_student_feedback(request):
   if request.method=="POST":
       feedback_id=request.POST.get('feedback_id')
       feedback_reply=request.POST.get("feedback_reply")

       feedback=Student_Feedback.objects.get(id=feedback_id)
       feedback.feedback_reply=feedback_reply
       feedback.status=1
       feedback.save()
       return redirect('send1_student_feedback')
   

import firebase_admin
from firebase_admin import credentials

