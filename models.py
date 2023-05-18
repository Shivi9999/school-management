from django.db import models
from datetime import datetime,timedelta
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
    )
from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
   

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):

    """ Main User config """
    email = models.EmailField(unique=True, verbose_name='Email Address')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    HOD = '1'
    STAFF = '2'
    STUDENT = '3'
    TRANSPORT_MANAGER='4'
    User_type=(
        ('hod','HOD'),
        ('staff','STAFF'),
        ('student','STUDENT'),
        ('transport_manager','TRANSPORT_MANAGER'),
       
    )
    user_type_data = ((HOD, "HOD"), (STAFF, "Staff"), (STUDENT, "Student"),(TRANSPORT_MANAGER, "transport_manager"))
    user_type = models.CharField( choices=user_type_data, max_length=10)
 
    profile_pic=models.ImageField(upload_to='media/profile_pic' ,null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_name']

    objects = UserManager()

    class Meta:
        db_table = 'user_profile'

    def __str__(self):

        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        # User permission
        return True

    def has_module_perms(self, app_label):
        # User permission to view the ap modules
        return True
class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.TextField(null=True)
    gender=models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)
    
    class Meta:
        verbose_name = ('AdminHOD')
        verbose_name_plural = ('AdminHODS')

    def save(self, *args, **kwargs):

        self.slug = slugify(self.user.first_name + '' + self.user.last_name)
        return super().save(*args, **kwargs)
    def __str__(self):

        return f"{self.user}"

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.TextField()
    gender=models.CharField(max_length=100)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    slug = models.SlugField(null=True)
    
    class Meta:
        verbose_name = ('Teacher')
        verbose_name_plural = ('Teachers')

    def save(self, *args, **kwargs):

        self.slug = slugify(self.user.first_name + '' + self.user.last_name)
        return super().save(*args, **kwargs)
    def __str__(self):

        return f"{self.user}"

class Course(models.Model):
    course=models.CharField(max_length=100)
   
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.course
    
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
   
    address=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING,null=True,blank=True)
   
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = ('Student')
        verbose_name_plural = ('Students')

    def save(self, *args, **kwargs):

        self.slug = slugify(self.user.first_name + '' + self.user.last_name)
        return super().save(*args, **kwargs)
    def __str__(self):

        return f"{self.user}"
class Subjects(models.Model):
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
     
    # need to give default course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject_name
class Transport_manager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    address=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = ('Transport')
        verbose_name_plural = ('Transports')

    def save(self, *args, **kwargs):

        self.slug = slugify(self.user.first_name + '' + self.user.last_name)
        return super().save(*args, **kwargs)
    def __str__(self):

        return f"{self.user}"
class bus_name(models.Model):
    bus_route=models.CharField(max_length=100)
    def __str__(self) :
        return self.bus_route
class Add_bus(models.Model):
    bus_number=models.CharField(max_length=200)
    registration_number=models.CharField(max_length=200)
    bus_route=models.ForeignKey(bus_name,on_delete=models.DO_NOTHING)
    def __str__(self) :
        return self.bus_number +" "+ self.bus_route
    
class Add_driver(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    contact_number=models.IntegerField()
    profile_pic=models.ImageField()
    date_of_joining=models.DateField(auto_now=True)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class intimation(models.Model):
    
    subject=models.CharField(max_length=500)
    email=models.EmailField(max_length=200)
    message=models.TextField()
    def __str__(self):
        return self.subject
class Quizequestion(models.Model):
    category=models.ForeignKey(Course,on_delete=models.CASCADE)
    question=models.CharField(max_length=500)
    option1=models.CharField(max_length=500)
    option2=models.CharField(max_length=500)
    option3=models.CharField(max_length=500)
    option4=models.CharField(max_length=500)
    level=models.CharField(max_length=100)
   
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=100)
    def __str__(self):
        return self.question
class Usersubmitans(models.Model):
    question=models.ForeignKey(Quizequestion,on_delete=models.CASCADE)
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    right_answer=models.CharField(max_length=100)
class Usersubmitattempt(models.Model):
    category=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    attempted_time=models.DateField(auto_now_add=True)
class Staff_notification(models.Model):
    staff_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    message=models.TextField()
    status=models.IntegerField(null=True,default=0)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.staff_id.user.first_name+"  " +self.staff_id.user.last_name
class staff_leave(models.Model):
    
    staff_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True)
    date=models.DateField(max_length=100)
    msg=models.TextField()
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.user.first_name +"  " +self.staff_id.user.last_name
class student_leave(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    msg=models.TextField()
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student_id.user.first_name +"  " +self.student_id.user.last_name
class Staff_Feedback(models.Model):
    staff_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    status=models.IntegerField(null=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_id.user.first_name+"  " +self.staff_id.user.last_name
class Student_notification(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    message=models.TextField()
    status=models.IntegerField(null=True,default=0)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.student_id.user.first_name+"  " +self.student_id.user.last_name
class Student_Feedback(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    status=models.IntegerField(null=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_id.user.first_name+"  " +self.student_id.user.last_name
class Writer_name(models.Model):
    writer_name=models.CharField(max_length=500)
    def __str__(self):
        return self.writer_name
class Book_entry(models.Model):
    book_name=models.CharField(max_length=500)

    book_code=models.CharField(max_length=500)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    writer_name=models.ForeignKey(Writer_name,on_delete=models.DO_NOTHING)
    price=models.CharField(max_length=500)
    author_name=models.CharField(max_length=500)
    date=models.DateField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    code=models.ImageField(blank=True,upload_to='code')
    def __str__(self)-> str:
        return self.book_name +self.book_code
    def save(self,*args,**kwargs):
        qr_image=qrcode.make(self.book_code + self.book_name +self.price)
        qr_offset=Image.new('RGB',(310,310),'white')
        qr_offset.paste(qr_image)
        files_name=f'{self.book_code+ self.book_name+self.price}-{self.id}qr.png'
        stream=BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(files_name,File(stream),save=False)
        qr_offset.close()
        super().save(*args,**kwargs)
    
def expiry():
    return datetime.today() + timedelta(days=15)
class IssuedBook(models.Model):
    # admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE) 
    book_code = models.CharField(max_length=788)
    book_name=models.ForeignKey(Book_entry,on_delete=models.CASCADE ,related_name='book_nm')
    contact_number=models.CharField(max_length=788)
    issued_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(default=expiry)
    quantity= models.IntegerField(default=0,null=True)
    
    def __str__(self):
        return self.student_name.user.first_name
    def save(self, *args, **kwargs):
        if not self.pk: # only for creating not for update:
            self.book_name.quantity = self.book_name.quantity - 1
            self.book_name.save()
        super().save(*args, **kwargs)
class Add_fees(models.Model):
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    #pay_fees=models.IntegerField(max_length=100,default=0)
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    fee_category=models.CharField(max_length=100)
    def __str__(self):
        return self.course.course