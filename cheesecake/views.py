#-*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse , HttpResponseRedirect   
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf.urls.static import static
from django.conf import settings

from datetime import datetime  
from cheesecake.models  import Cake,VisitorTime,Comment,Buy 
from cheesecake.forms  import CommentForm, BuyForm, Customer_infoForm
from cheesecake.Visitor  import *
from django import forms
from django.views.generic.edit import FormView 
from django.views.generic.base import TemplateView
import json

def home(request):

    #前置
    request.session['uesr_id'] = Session.objects.count() +1     #set sessions
    request.session.set_expiry(300)  #set sessions
    request.session.clear_expired()   #set sessions
    #解決Session.objects算不到的問題
    #可否嘗試用settinterval 概念 每十分鐘就利用Function發出Request 抓取Count數值 並存到Models裡
    set_interval(data_to_SQL, 10)# transfer visitor data to SQL
    #session過期時間應該跟抓取時間一致才能統計'一個間隔'內的上線數

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

        nickname=form.cleaned_data['Nickname']
        email=form.cleaned_data['Email']
        cakeflavor=form.cleaned_data['Cakeflavor']#!!這邊傳回來的是list(MultipleChoiceField),但傳給model那邊會把它變成str(charField),待解決
        content=form.cleaned_data['Content']

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
    success_url = '/Buy/'

    def form_valid(self,form):
        #session新增一dict內dict, = >request.session = {'Buy_info': [('抹茶', 3),()....] , ...}
        if  'Buy_info' not in self.request.session:
            self.request.session['Buy_info'] = []           
        
        self.request.session['Buy_info'].append( (form.cleaned_data['Cakeflavor'], form.flavortoCost(), form.cleaned_data['Number'] ))

        return super(BuyFormView,self).form_valid(form)

# In views.py :
# 1.BuyFormView:利用session暫存購物車內容(設置一個加入購物車input),且此頁只有選商品跟數量功能 
# 2.CartCountView(填寫地址(也是利用session暫存)&顯示購物內容&設置一個結帳input)
# 3.SucceccView: 顯示購物成功價錢與匯款資訊,並把session內容通通存到modelDB內

class CartCountView(FormView): 

    template_name ='CartCount.html'
    form_class = Customer_infoForm   
    success_url = '/Success/'

    def get_context_data(self, **kwargs):
       
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()

        #要是不小心太久沒結帳,session過期了, =>
        if 'Buy_info' not in self.request.session:
            self.request.session['Warning_info'] = ['您太久沒結帳!請重新選擇商品!']
            kwargs['Warning_info'] = self.request.session['Warning_info']         
            return super(CartCountView, self).get_context_data(**kwargs)

        #在此加入上一頁訂單資訊(是一個dict, ex:{'抹茶': 3 } ),才能夠在購物車結帳頁計算顯示總價
        kwargs['Buy_info'] = self.request.session['Buy_info']         
        return super(CartCountView, self).get_context_data(**kwargs)

#這邊是結合購物車顯示與填寫地址功能 並有個btn能連到SuccessView


class SuccessView(TemplateView):
    pass
#顯示購物成功價錢與匯款資訊,並把session內容通通存到modelDB內
#記得最後結帳完要清空session,不然同一個人再登入會累加之前帳單