from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages
def home(request):
    return render(request,'transport/transport_home.html')
def add_bus(request):
    bus111=bus_name.objects.all()
    if request.method=="POST":
        bus_number=request.POST.get('bus_number')
        registration_number=request.POST.get('registration_number')
        bus_route=request.POST.get('bus_route')
        bus_row=bus_name.objects.get(id=bus_route)
        bus1=Add_bus(bus_number=bus_number,registration_number=registration_number,bus_route=bus_row)
        bus1.save()
        messages.success(request,'Data is saved successfully!')
        return redirect('add_bus')
   
    return render(request,'transport/add_bus.html',{'bus111':bus111})
def edit_bus(request,id):
    edit_bus=Add_bus.objects.get(id=id)
    bus111=bus_name.objects.all()
    context={'edit_bus':edit_bus,'bus111':bus111}
    return render(request,'transport/edit_bus.html',context)
def update_bus(request):
   

    if request.method=="POST":
      bus_number=request.POST.get('bus_number')
      registration_number=request.POST.get('registration_number')
      bus_route_id=request.POST.get('bus_route_id')
      bus_id=request.POST.get('bus_id')
      bus_route=bus_name.objects.get(id=bus_route_id)
      edit1=Add_bus(id=bus_id,bus_number=bus_number,registration_number=registration_number,bus_route=bus_route)
     
      
      edit1.save()
      messages.success(request,'Data Updated succssefully')  
      return redirect('view_bus')
    return render(request,'transport/edit_bus.html')
def add_driver(request):
   
     if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         contact_number=request.POST.get('contact')
         profile_pic=request.FILES.get('profile_pic')
         date_of_joining=request.POST.get('date_of_joining')
         address=request.POST.get('address')
   
         driver=Add_driver(name=name,email=email,contact_number=contact_number,profile_pic=profile_pic,date_of_joining=date_of_joining,address=address)
         driver.save()
         messages.success(request,'Data Added Successfully')
         return redirect('add_driver')
     return render(request,'transport/add_driver.html')
def view_bus(request):
    bus=Add_bus.objects.all()
    return render(request,'transport/view_bus.html',{'bus':bus})
def view_driver_transport(request):
    driver=Add_driver.objects.all()
    context={'driver':driver}
    return render(request,'transport/view_driver.html',context)
def edit_driver(request,id):
    driver=Add_driver.objects.get(id=id)
    context={'driver':driver}
    return render(request,'transport/edit_driver.html',context)
def update_driver(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact_number=request.POST.get('contact')
        profile_pic=request.FILES.get('profile_pic')
        date_of_joining=request.POST.get('date_of_joining')
        address=request.POST.get('address')
        driver_id=request.POST.get('driver_id')
        
        driver=Add_driver.objects.get(id=driver_id)
        if profile_pic!=None and profile_pic!="":
            driver.profile_pic=profile_pic 
        driver.name=name
        driver.email=email
        driver.contact_number=contact_number
      
        driver.date_of_joining=date_of_joining
        driver.address=address
        driver.save()
        messages.success(request,'Data Updated succssefully')  
        return redirect('view_driver_transport')
    return render(request,'transport/edit_driver.html')
# def change_bus_route(request):
#     bus=Add_bus.objects.all()
#     bus1=change_route.objects.all()
#     if request.method=="POST":
#         bus_number=request.POST.get('bus_number')
#         bus_route11=request.POST.get('bus_route')
#         station=request.POST.get('station')
#         bus_rou=Add_bus.objects.get(id=bus_route11)
#         bus_num=Add_bus.objects.get(id=bus_number)
#         book=change_route(bus_number=bus_num,bus_route11=bus_rou,station=station)
#         book.save()
#         return redirect('change_bus_route')
#     context={'bus':bus,'bus1':bus1}
#     return render(request,'transport/change_busroute.html',context)  