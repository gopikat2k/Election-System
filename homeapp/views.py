from django.shortcuts import render
from .models import adminlog

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        email = request.POST.get('eml')
        password = request.POST.get('psw')
        obj = adminlog.objects.filter(email = email ,password = password)
        if obj:
            return render(request, "home.html")
        else:
            return render(request,"adminlog.html")
    else:
        return render(request,"adminlog.html")
