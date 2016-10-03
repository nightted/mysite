#-*- coding: utf-8 -*-
import threading
from cheesecake.models  import Visitor ,Buy
from django.contrib.sessions.models import Session 
from datetime import datetime



def set_interval(func, sec):
	
    	def func_wrapper():
        		set_interval(func, sec) 
        		func()  

    	t = threading.Timer(sec, func_wrapper)
    	t.start()
    	


def Visitor_Count():

	onlinepeople=0
	for sess in Session.objects.all():
		if  datetime.now() < sess.expire_date:
			onlinepeople+=1

	return onlinepeople

#
def data_to_SQL ():

	VisitorTime.objects.create(number=Visitor_Count())
	if  VisitorTime.objects.count() >= 100:
		VisitorTime.objects.all()[0].delete()


def cake_Count():
	
	number_cake=[0,0,0,0]

	for item in Buy.objects.all():

		n=0
		buynumber=eval(item.Buynumber)
		for flavor in item.Cakeflavor.all():

			
			if flavor.CakeName == u'原味':
				number_cake[0]+= buynumber[n]
			if flavor.CakeName == u'抹茶紅豆':
				number_cake[1]+= buynumber[n]
			if flavor.CakeName == u'芝麻':
				number_cake[2]+= buynumber[n]
			if flavor.CakeName == u'蔓越莓':
				number_cake[3]+= buynumber[n]
			n+=1

	return number_cake

#set_interval(data_to_SQL, 10)
