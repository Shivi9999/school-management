from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def base(request):
    return render(request, 'base.html')
def Login(request):
    return render(request,'login_page.html')
def doLogin(request):
     
   if request.method=='POST':
        user=authenticate(request,
                                       username=request.POST.get('email'),
                                       password=request.POST.get('password'),)
        if user!=None:
            login(request,user) 
            user_type=user.user_type
            if user_type==User.HOD:
               return redirect('Hod_home')
            elif user_type==User.STAFF:
               return redirect('staff_home')
            elif user_type==User.STUDENT:
               
                return redirect('student_home')
            elif user_type==User.TRANSPORT_MANAGER:
               
                return redirect('transport_home')
            else:
                messages.error(request,'invalid credentials')
                return redirect('login')
        else:
            messages.error(request,'invalid credentials')

   return redirect('login')
@login_required(login_url='/')
def profile(request):
    user=User.objects.get(id=request.user.id)
    context={
        'user':user,
        }
    return render(request,'profile.html',context)
@login_required(login_url='/')
def profile_update(request):
    if request.method=="POST":
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        #username=request.POST.get('username')
        #email=request.POST.get('email')
        password=request.POST.get('password')
        print(profile_pic)
        try:
            customuser=User.objects.get(id=request.user.id)
            customuser.first_name= first_name
            customuser.last_name= last_name
            #customuser.profile_pic= profile_pic
            #customuser.profile_pic=request.FILES.get('profile_pic')
            if password!=None and password!="":
                customuser.set_password(password)
            if profile_pic!=None and profile_pic!="":
                 customuser.profile_pic=profile_pic
            customuser.save()
            messages.success(request,'profile updated succussefully')
            return redirect('profile')
        except:
            messages.error(request,' Failed profile is Not updated')
    return render(request,'profile.html')

def signup_as_a_student(request):
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
           return redirect('signup_as_a_student')
       elif User.objects.filter(user_name=user_name).exists():
           messages.error(request,'username is already exist')
           return redirect('signup_as_a_student')
       else:
           user=User(first_name=first_name,last_name=last_name,email=email,user_name=user_name,profile_pic=profile_pic, user_type=3)
           user.set_password(password)
           user.save()
        #    subject='about registration  '
        #    otp=random.randint(1000,9999)
        #    from_email='b97ciss@gmail.com'
        #    msg='your otp  is otp  '
        #    to =request.POST.get('Email')
            
        #    msg=EmailMultiAlternatives(subject,msg,from_email,[to])
        #    msg.send()
           course=Course.objects.get(id=course_id)
          
           student=Student(
               admin=user,
               address=address,
            
               course_id=course,
               Gender=Gender
           )
           student.save()
           messages.success(request,'Data is saved successfully!')
           return redirect('signup_as_a_student')
       
    context={'course':course}

    return render(request,'includes/signup_as_a_student.html',context)
     
def signup_as_a_admin(request):
   if request.method=="POST":
       profile_pic=request.FILES.get('profile_pic')
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       email=request.POST.get('email')
       user_name=request.POST.get('username')
       password=request.POST.get('password')
       address=request.POST.get('address')
       gender=request.POST.get('Gender')
       if User.objects.filter(email=email).exists():
           messages.error(request,'Email is already exist')
           return redirect('signup_as_a_admin')
       elif User.objects.filter(user_name=user_name).exists():
           messages.error(request,'username is already exist')
           return redirect('signup_as_a_admin')
       else:
           user=User(first_name=first_name,last_name=last_name,email=email,user_name=user_name,profile_pic=profile_pic, user_type=1)
           user.set_password(password)
           user.save()
          
           manager=AdminHOD(
               user=user,
               address=address,
              
               gender=gender
           )
           manager.save()
           messages.success(request,'Data is saved successfully!')
           return redirect('signup_as_a_admin')
    
   
    
   return render(request,'includes/signup_as_a_admin.html')
     
def doLogout(request):
  logout(request)
  return redirect('login')