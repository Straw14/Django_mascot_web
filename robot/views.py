from django.shortcuts import render
from django.http import HttpResponse
from robot.models import Parameter 
from robot.models import Inventory
#import RPi.GPIO as GPIO
import time
import os
import serial


ser = serial.Serial('/dev/ttyACM0', 9600) 
time.sleep(3)

def home(request):
	a= Inventory.objects.get(id='1')
	return render(request, 'homeweb.html',{'data':a.identify})

def finger(request):
	while True:
		a= Inventory.objects.get(id='1')
		su = a.identify
		print(su)
		ser.write(su.encode())
		time.sleep(10)
		break
		
	return render(request, 'homeweb.html',{'data':a.identify})

def TP(request):
	from Straw.wsgi import thread_loop
	if request.method == "POST":
		sp1 = request.POST.get("sp1", None)
		ang1 = request.POST.get("ang1", None)
		dis1 = request.POST.get("dis1", None)
		
		sp2 = request.POST.get("sp2", None)
		ang2 = request.POST.get("ang2",None)
		dis2 = request.POST.get("dis2",None)
		
		sp3 = request.POST.get("sp3",None)
		ang3 = request.POST.get("ang3",None)
		dis3 = request.POST.get("dis3",None)
		twz = Parameter.objects.create(sp1=sp1,ang1=ang1,dis1=dis1,sp2=sp2,ang2=ang2,dis2=dis2,sp3=sp3,ang3=ang3,dis3=dis3)
		twz.save()		
		su="1="+str(sp1)+","+str(ang1)+","+str(dis1)+",2="+str(sp2)+","+str(ang2)+","+str(dis2)+",3="+str(sp3)+","+str(ang3)+","+str(dis3)
		print(su)
		ser.write(su.encode())
	
	return render(request, 'homeweb.html')
