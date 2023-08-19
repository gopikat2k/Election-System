from django.shortcuts import render
from .models import userregi

# Create your views here.
def index(request):
    return render(request,"userregi.html")
def regi(request):
    if request.method == 'POST':

        Fullname= request.POST.get('Fullname')
        Phonenumber = request.POST.get('phonenumber')
        Address = request.POST.get('address')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Uploadid= request.POST.get('Uploadid')

        obj = userregi.objects.create(Fullname=Fullname,Phonenumber=Phonenumber,Address=Address,Email=Email,Password=Password,Uploadid=Uploadid)
        obj.save()
        if obj:
            return render(request, "userlog.html")
        else:
            return render(request,"userregi.html")
    else:
        return render(request,"userregi.html")
    
def userlogin(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        obj = userregi.objects.filter(Email=Email,Password=Password)
        if obj:
            return render(request, "userhome.html")
        else:
            return render(request,"userlog.html")
    else:
        return render(request,"userlog.html")