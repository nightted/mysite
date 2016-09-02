#-*- coding: utf-8 -*-
import os,time,sys
from Tkinter import *
import tkMessageBox

def tk(str1):
	
	top = Tk()
	top.title("Hello Test")

	def btnHelloClicked():
	                
	    tkMessageBox.showwarning("Warning", "該睡覺了!!很乖!!")
	    top.destroy()	 
		
	labelHello = Label(top, text = str1 , height = 50, width = 200,fg = "red")
	labelHello.pack()

	btn = Button(top, text = "確定!", command = btnHelloClicked, height = 10, width = 180,fg = "blue")
	btn.pack()	 
		
	top.mainloop()


class TimeCmp:
    def __init__(self, TimeStart, TimeEnd):
        self.TimeStart=TimeStart
        self.TimeEnd=TimeEnd

    def Cmp(self):
        LocalTime=time.localtime(time.time())
        self.__TimeNow_1=LocalTime.tm_hour*3600+LocalTime.tm_min*60+LocalTime.tm_sec
        self.__TimeStart_1=3600*self.TimeStart[0]+60*self.TimeStart[1]+self.TimeStart[2]
        self.__TimeEnd_1=3600*self.TimeEnd[0]+60*self.TimeEnd[1]+self.TimeEnd[2]
        
        if self.__TimeEnd_1 - self.__TimeNow_1 < 10 :
            return True
        else:
            return False


def run():

	hr = input("Time you wamt to close your computer(Hrs):")
	minute = input("Time you wamt to close your computer(Minutes):")
	TimeStart=(8,0,0)
	TimeEnd=(int(hr),int(minute),00)
	SystemCmd="c:\\windows\\SysWoW64\\Shutdown -s -t 60"

	while True:

		TimeCmpResult=TimeCmp(TimeStart, TimeEnd)#print TimeCmpResult.Cmp()
		shutdown=TimeCmpResult.Cmp()

		LocalTime=time.localtime(time.time())
		__TimeNow_1=LocalTime.tm_hour*3600+LocalTime.tm_min*60+LocalTime.tm_sec
		__TimeEnd_1=3600*TimeEnd[0]+60*TimeEnd[1]+TimeEnd[2]
		deltatime = __TimeEnd_1 - __TimeNow_1
		

		if shutdown:
			tk("剩"+str(deltatime)+"秒鐘關機!")            			
			
			
			os.system(SystemCmd)
		else:
			pass

		time.sleep(float(60))

if __name__=="__main__":

    run()
