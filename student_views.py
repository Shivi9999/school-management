from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from app import forms
from django.conf import settings
from django.utils import timezone
from app import models as QMODEL
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.base import TemplateView
@login_required(login_url='/')
def home(request):
    return render(request,'student/student_home.html')
@login_required(login_url='/') 
def student_noti(request):
    student=Student.objects.filter(user=request.user.id)
    for i in student:
       student_id=i.id
       notification=Student_notification.objects.filter(student_id=student_id)
       context={'notification':notification}
       return render(request,'student/notify.html',context)
@login_required(login_url='/') 
def mark_as_done1(request,status):
    notification=Student_notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('stud_notification')
@login_required(login_url='/') 
def student_feedback(request):
    leave=Student.objects.filter(user=request.user.id) 
    for x in leave:
        student_id=x.id

        student_feedback=Student_Feedback.objects.filter(student_id=student_id)
     
        context={'student_feedback':student_feedback}
        return render(request,'student/student_feedback.html',context)
@login_required(login_url='/') 
def save_student_feedback(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        student=Student.objects.get(user=request.user.id)
        feedback=Student_Feedback(student_id=student,feedback=feedback,feedback_reply="")
        feedback.save()
        return redirect('student_feedback')
@login_required(login_url='/') 
def student_apply_leave(request):
    leave=Student.objects.filter(user=request.user.id) 
    for x in leave:
        student_id=x.id

        student_leave1=student_leave.objects.filter(student_id=student_id)
     
        context={'student_leave1':student_leave1}

    return render(request,'student/apply_leave1.html',context)

@login_required(login_url='/')
def student_apply_leave_save(request):
    if request.method=="POST":
        date=request.POST.get('date')
        msg=request.POST.get('msg')
        student=Student.objects.get(user=request.user.id)
        save_leave=student_leave(student_id=student,date=date,msg=msg)
        save_leave.save()
        return redirect('student_apply_leave')

def view_book(request):
    book_entry=Book_entry.objects.all()
  
    return render(request,'student/view_book.html',{'book_entry':book_entry})
def view_issue_book(request):
    student = Student.objects.get(user=request.user.id)
    book_entry = IssuedBook.objects.filter(student_name_id=student.id)
    # book_entry=IssuedBook.objects.all()
    return render(request,'student/view_issue_book.html',{'book_entry':book_entry})
def fees_submit(request):
    student_name=Student.objects.all()
    course=Course.objects.all()

    context={'student_name':student_name,'course':course}
    return render(request,'student/fees.html',context)
def fees_submit_save(request):
     if request.method=="POST":
         course=request.POST.get('course')
         student_name=request.POST.get('student_name')
         fee_category=request.POST.get('student_name')
         course1=Course.objects.get(id=course)
         student_name1=Student.objects.get(id=student_name)
         fee=Add_fees(course=course1,student_name=student_name1,fee_category=fee_category)
         fee.save()
         return redirect('paytm')
class paytm(TemplateView):    
  
    template_name = 'student/paytm.html'
    def get_context_data(self, **kwargs): # new         
          context =super().get_context_data(**kwargs)        
          context['key'] = settings.PUBLISHABLE_KEY        
          return context
    
def success(request):
    return render(request,'student/succses.html')

from django.urls import reverse
# from paypal.standard.forms import PayPalPaymentsForm

class paypal(TemplateView):
    template_name = 'student/paypal.html'


# def Exam(request):
#     student=Student.objects.filter(admin=request.user.id)
#    # subject=Subject.objects.filter(subject_name=request.user.id)
#     for i in student :
#         course_id=i.id
      
#         task=Student.objects.filter(course_id=course_id)
#         context={'task':task,'student':student}
#     return render(request,'student/exam.html',context)  

def student_exam_view(request):
    student = Student.objects.get(user=request.user.id)
    courses = Course.objects.filter(student=student.id)
    #courses=Course.objects.filter(student_result)
    return render(request,'student/student_exam.html',{'courses':courses})

@login_required(login_url='/')

def take_exam_view(request,id):
    
    category=QMODEL.Course.objects.get(id=id)
    total_questions=QMODEL.Quizequestion.objects.all().filter(category=category).count()
    questions=QMODEL.Quizequestion.objects.all().filter(category=category)
    # total_marks=0
    # for q in questions:
    #     total_marks=total_marks + q.marks
    
    return render(request,'student/take_exam.html',{'category':category,'total_questions':total_questions})

@login_required(login_url='/')

def start_exam_view(request,id):
    category=Course.objects.get(id=id)
    question=Quizequestion.objects.filter(category=category).order_by('id').first()
    return render(request,'student/start_exam.html',{'question':question,'category':category})
    # category=QMODEL.Course.objects.get(id=id)
    # questions=QMODEL.Quizequestion.objects.all().filter(category=category)
    # if request.method=='POST':
    #     pass
    # response= render(request,'student/start_exam.html',{'category':category,'questions':questions})
    # response.set_cookie('category_id',category.id)
    # return response
@login_required
def submit_answer(request,cat_id,quest_id):
    percentage=None
    if request.method=="POST":
        category=Course.objects.get(id=cat_id)
        question=Quizequestion.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest=Quizequestion.objects.get(id=quest_id)
                student = Student.objects.get(user=request.user.id)
                answer='Not submitted'
                Usersubmitans.objects.create(user=student,question=quest,right_answer=answer)
                return render(request,'student/start_exam.html',{'question':question,'category':category})
        
        else: 
            student = Student.objects.get(user=request.user.id)
            result=Usersubmitans.objects.filter(user=student.id)
            quest=Quizequestion.objects.get(id=quest_id)
            user=request.user
            answer=request.POST['answer']
            Usersubmitans.objects.create(user=student,question=quest,right_answer=answer)
        if question:
            return render(request,'student/start_exam.html',{'question':question,'category':category,'result':result})
        else:
            student=Student.objects.get(user=request.user.id)
            total_questions=QMODEL.Quizequestion.objects.all().filter(category=category).count()
            result=Usersubmitans.objects.filter(user=student.id)
            skipped=Usersubmitans.objects.filter(user=student.id,right_answer="Not submitted").count()
            attempted=Usersubmitans.objects.filter(user=student.id).exclude(right_answer="Not submitted").count()
            rightAns=0
            for row in result:
                percentage=0
                if row.question.right_opt  == row.right_answer: 
                     rightAns+=1
                percentage=(rightAns*100)/result.count()
            
            return render(request,'student/result.html',{'result':result,'total_skipped':skipped,'total_attempted':attempted,'total_questions':total_questions,'rightAns':rightAns,'percentage':percentage})
        
    else:
        return HttpResponse("Method is not allowed!")

# def result(request):
#     student = Student.objects.get(admin=request.user.id)
#     courses = Course.objects.filter(student=student.id)
#     return render(request,'student/view_result.html',{'courses':courses})

    
# def check_marks_view(request,pk):
#     course=Course.objects.get(id=pk)
#     student = Student.objects.get(admin_id=request.user.id)
#     results=Quizequestion.objects.all().filter(question=course).filter(category=student)
#     return render(request,'student/check_marks.html',{'results':results})


   
   
   
   