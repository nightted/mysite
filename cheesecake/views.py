#-*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse , HttpResponseRedirect   
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf.urls.static import static
from django.conf import settings

from datetime import datetime  
from cheesecake.models  import Cake,VisitorTime,Comment,Buy 
from cheesecake.forms  import CommentForm,BuyFrom
from cheesecake.Visitor  import *
from django.views.generic.edit import FormView 
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
                           



class CommentFormView(FormView):
    template_name= 'Comment.html'
    form_class = CommentForm
    

    def form_valid(self, form):

        nickname=self.request.POST['Nickname']
        email=self.request.POST['Email']
        cakeflavor=self.request.POST['Cakeflavor']
        content=self.request.POST['Content']

        Comment.objects.create(Nickname=nickname,Email=email,Flavor=cakeflavor,Content=content )
        
        self.request.method='GET' #使填完後清空欄位(get_form_kwargs裡的判斷)
        c=self.get_context_data() #填完也繼續顯示出空白的填單
        c['messages']=Comment.objects.all()

        return self.render_to_response(c)

    def get(self, request, *args, **kwargs): 
        #讓剛進還沒填過的人也看的到先前的留言

        c=self.get_context_data()
        c['messages']=Comment.objects.all()
        return self.render_to_response(c)


class BuyFormView(FormView):

    template_name ='Buy.html'
    form_class = BuyForm   
    success_url = '/success/'

    def form_valid(self,form):

        customer_name=self.request.POST['Customer_name']
        address=self.request.POST['Address']
        phonenumber=self.request.POST['Phonenumber']
        email=self.request.POST['Email']
        cakeflavor=self.request.POST['Cakeflavor']
        number=self.request.POST['Number']

        Buy.objects.create(Customer_name=customer_name,Address=address,Phonenumber=phonenumber,Email=email,Cakeflavor=cakeflavor,Number=number )

class SucceccView():
