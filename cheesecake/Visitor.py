import threading
from cheesecake.models  import VisitorTime
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



#set_interval(data_to_SQL, 10)
