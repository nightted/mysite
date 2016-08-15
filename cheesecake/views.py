#-*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse , HttpResponseRedirect   
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf.urls.static import static
from django.conf import settings

from datetime import datetime
from cheesecake.models  import Cake ,VisitorTime
from cheesecake.Visitor  import * 
import json

def home(request):

    #前置
    request.session['uesr_id'] = Session.objects.count() +1     #set sessions
    request.session.set_expiry(300)  #set sessions
    request.session.clear_expired()   #set sessions
    #解決Session.objects算不到的問題
    #可否嘗試用settinterval 概念 每十分鐘就利用Function發出Request 抓取Count數值 並存到Models裡
    set_interval(data_to_SQL, 10)# transfer visitor data to SQL
    #前置

    number=[]
    t=[]
    for i in VisitorTime.objects.all():
            number.append(int(i.number))
            a="{0}月{1}日 - {2}:{3}:{4}".format(i.time.strftime('%m'),i.time.strftime('%d'),i.time.strftime('%H'),i.time.strftime('%M'),i.time.strftime('%S'))
            t.append(a)

    time=json.dumps(t)  #這邊要注意 "str" list 要在<script> 內顯示需要先編碼成json


    return render(request, 'home.html', {'time':time , 'number':number})
                           



def session_test(request):

    sid = request.COOKIES['sessionid']
  
