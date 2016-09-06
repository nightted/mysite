#-*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf.urls.static import static
from django.conf import settings

import threading
from datetime import datetime
from cheesecake.models  import Cake,VisitorTime,Comment,Buy
from cheesecake.forms  import CommentForm, BuyForm, Customer_infoForm
from cheesecake.Visitor_CakeNumber  import *
from django import forms
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
import json

class VisitorTimeMixin(object):

    def set_interval(self,func,sec):
    
        def func_wrapper():
            self.set_interval(func, sec) 
            func()  

        t = threading.Timer(sec, func_wrapper)
        t.start()
        


    def Visitor_Count(self):

        onlinepeople=0
        for sess in Session.objects.all():
            if  datetime.now() < sess.expire_date:
                onlinepeople+=1

        return onlinepeople

    
    def data_to_SQL(self):

        if  VisitorTime.objects.count() > 20:
            for i in range(0,VisitorTime.objects.count()-20):
                VisitorTime.objects.all()[0].delete()
   
        VisitorTime.objects.create(number=self.Visitor_Count())
   
        
        
    def cake_Count(self):
        
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




class HomeView(TemplateView,VisitorTimeMixin):
    
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        number_people=[]
        t=[]
        for i in VisitorTime.objects.all():
                number_people.append(int(i.number))
                a="{0}月{1}日 - {2}:{3}:{4}".format(i.time.strftime('%m'),i.time.strftime('%d'),i.time.strftime('%H'),i.time.strftime('%M'),i.time.strftime('%S'))
                t.append(a)

        time=json.dumps(t)  #(O)這邊要注意 "str" list 要在<script> 內顯示需要先編碼成json
        number_cake = self.cake_Count()
        Cakes = Cake.objects.all()

        kwargs.update({'time':time , 
                    'number_people':number_people ,
                    'number_cake':number_cake ,
                    'Cakes':Cakes})

        return super(HomeView,self).get_context_data(**kwargs)
    
    def get(self, request, *args, **kwargs): 
        #前置
        #%% Django only saves to the session database when the session has been modified!!!
        
        request.session['uesr_id'] = Session.objects.count() +1     #set sessions
        request.session.set_expiry(600)  #set sessions expiry
        request.session.clear_expired()   #clear expired sessions
        #(X)解決Session.objects算不到的問題
        #(O)嘗試用settinterval 概念 每十分鐘就利用Function發出Request 抓取Count數值 並存到Models裡
        self.set_interval(self.data_to_SQL,600)# transfer visitor data to SQL
        
        #session過期時間應該跟抓取時間一致才能統計'一個間隔'內的上線數

        return super(HomeView,self).get(self, request, *args, **kwargs)


class PostdetailView(DetailView):
    pass


class CommentFormView(FormView):
    template_name= 'Comment.html'
    form_class = CommentForm
    success_url = '/Comment/'


    def form_valid(self, form):       
        list = form.cleaned_data

        Comments=Comment.objects.create(Nickname=list['Nickname'],Email=list['Email'],Content=list['Content'] )
        Comments.save()

        for cakename in form.cleaned_data['Cakeflavor']: #manytomanyField add
            Comments.Flavor.add(Cake.objects.get(CakeName=cakename))
        
        return super(CommentFormView,self).form_valid(form)

    def get(self, request, *args, **kwargs):
        #(O)讓剛進還沒填過的人也看的到先前的留言
        c=self.get_context_data()
        c['messages']=Comment.objects.all()
        return self.render_to_response(c)


class BuyFormView(FormView):

    template_name ='Buy.html'
    form_class = BuyForm
    success_url = '/Buy/'

    def form_valid(self,form):
        ## (O)使用manytomanyField : Cake  --(many to many)-->  Buy, 如此一來可以使最後model_init的Cakeflavor用obj填入表示
        ## (O)讀取方面 : Cake  --(many to many)-->  Buy , so => Buy.Cakeflavor.all() vs. Cake.buy_set.all() 
        ## (O)Cake_obj.cakename = form.cleaned_data['Cakeflavor'], then => .append([Cake_obj])

        #session新增一dict內dict, = >request.session = {'Buy_info': [['抹茶', 300, 3 ,900],[]....] , ...}
        if  'Buy_infos' not in self.request.session: #第一次進來
            self.request.session['Buy_infos'] = []
            self.request.session['Buy_infos'].append( [form.cleaned_data['Cakeflavor'], form.flavortoCost(), form.cleaned_data['Number'], form.cleaned_data['Number']*form.flavortoCost()] )
        
        else: #第二次進來,檢查是否有重複口味,有的話合併訂單,沒就創新的單
            list = self.request.session['Buy_infos']
            index = [i for i in range(0,len(list)) if form.cleaned_data['Cakeflavor'] == list[i][0] ]

            if index:
                index=index[0]
                list[index][2] += form.cleaned_data['Number']
                list[index][3] += form.cleaned_data['Number']*form.flavortoCost()

            else:
                list.append( [form.cleaned_data['Cakeflavor'], form.flavortoCost(), form.cleaned_data['Number'], form.cleaned_data['Number']*form.flavortoCost()] )
        
        list = self.request.session['Buy_infos']
        self.request.session['Total_price'] = sum([list[i][3] for i in range(0,len(list))]) #結算總價,存在另一個dict key中

        return super(BuyFormView,self).form_valid(form)

# In views.py :
## (O)1.BuyFormView:利用session暫存購物車內容(設置一個加入購物車input),且此頁只有選商品跟數量功能 
## (O)2.CartCountView(填寫地址(也是利用session暫存)&顯示購物內容&設置一個結帳input)
## (O)3.SucceccView: 顯示購物成功價錢與匯款資訊,並把session內容通通存到modelDB內

class CartCountView(FormView):

    template_name ='CartCount.html'
    form_class = Customer_infoForm
    success_url = '/Success/'

    def get_context_data(self, **kwargs):

        #刪除指定的購物清單內容
        if 'Buy_infos' in self.request.session:

            if 'id' in self.request.GET and 'stop' not in self.request.session:

                delete_index = int(self.request.GET['id'])
                del self.request.session['Buy_infos'][delete_index]

                #if len(self.request.session['Buy_infos']) == 0 : #(X)BUG!!!!!! 重新整理會不斷的刪掉訂單!!
                #   self.request.session['stop'] = 'stop'

            kwargs['Buy_infos'] = self.request.session['Buy_infos']
            kwargs['Total_price'] = self.request.session['Total_price'] # 顯示~
            return super(CartCountView, self).get_context_data(**kwargs)

        ##(X)要是不小心太久沒結帳,session過期了, =>
        else :
            kwargs['Warning_infos'] = '您太久沒結帳!請重新選擇商品!' #BUG!!!! 顯示不出來!!          
            return super(CartCountView, self).get_context_data(**kwargs)


    def form_valid(self,form):

        self.request.session['Customer_infos'] = []
        self.request.session['Customer_infos'].append( [form.cleaned_data['Customer_name'], form.cleaned_data['Address'], form.cleaned_data['Phonenumber'], form.cleaned_data['Email'], form.cleaned_data['Catchmethod'],form.cleaned_data['Catchlocation']] )
       
        ##(X)加入send_mail,顧客訂單一送出就傳mail通知~
        '''
        form.sendmail(self.request.session['Buy_infos'])
        '''
        ##(X)這裡加上try , expect敘述 , 以防蛋糕表單是空的拋出例外~
        return super(CartCountView,self).form_valid(form)

        #這邊是結合購物車顯示與填寫地址功能 並有個btn能連到SuccessView


class SuccessView(TemplateView):
    
    template_name = 'success.html'

    def get_context_data(self, **kwargs):

        S_B = self.request.session['Buy_infos'] 
        S_C = self.request.session['Customer_infos'][0]

        f_list = [list[0] for list in S_B]
        n_list = [list[2] for list in S_B]        
        
        
        Buytotal = Buy.objects.create(Customer_name=S_C[0],Address=S_C[1],Phonenumber=S_C[2],Email=S_C[3],Catchmethod=S_C[4],Catchlocation=S_C[5],Buynumber=n_list )
        Buytotal.save()       

        for cakename in f_list:
            Buytotal.Cakeflavor.add(Cake.objects.get(CakeName=cakename))        

        ##(O)目前問題 : 現在已經製造物件Cake , BUT 無法成功使用add 混入Buytotal中!!!         
        kwargs['Total_infos'] = Buytotal
        kwargs['Total_price'] = self.request.session['Total_price']
        #kwargs['test'] = str(type(Buytotal.Buynumber)) 
        
        return super(SuccessView, self).get_context_data(**kwargs)


    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        #刪除客戶訂單個資       
        del self.request.session['Buy_infos']
        del self.request.session['Customer_infos']
        del self.request.session['Total_price']

        return self.render_to_response(context)

##(O)顯示購物成功價錢與匯款資訊,並把session內容通通存到modelDB內
##(O)記得最後結帳完要清空session,不然同一個人再登入會累加之前帳單

