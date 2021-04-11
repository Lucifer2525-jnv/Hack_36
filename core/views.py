from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.
def emergency(request,name,phone,email,location):
    obj = API(name = str(name),phone = int(phone),email=email,location=str(location))
    obj.save()
    return JsonResponse({'status': 'OK'})

def home(request):
    obj = API.objects.all()
    return render(request,'base.html',{'obj':obj})