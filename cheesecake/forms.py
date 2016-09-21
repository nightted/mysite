# -*- coding: UTF-8 -*-
from django import forms
from django.core.mail import send_mail


class CommentForm (forms.Form):
	
	Nickname = forms.CharField(max_length=20,label='您的暱稱')
	Email = forms.EmailField(max_length=100,label='您的Email',required=False,help_text='(非必填)')
	Cakeflavor = forms.MultipleChoiceField(label='您訂購的口味',widget=forms.CheckboxSelectMultiple,choices= (
		('原味','原味'),
		('抹茶紅豆','抹茶紅豆'),
		('芝麻','芝麻'),
		('蔓越莓','蔓越莓'),
	))
	Content = forms.CharField(max_length = 500 ,label='您的評論')
	


#add購物車
class BuyForm(forms.Form):

	Cakeflavor = forms.ChoiceField(label='您訂購的口味',choices= (
		('原味','原味'),
	    ('抹茶紅豆','抹茶紅豆'),
	    ('芝麻','芝麻'),
	    ('蔓越莓','蔓越莓'),
	))
	Number = forms.IntegerField(label='您訂購的數量',localize= False,max_value=100,min_value=0)

	def flavortoCost(self):

		# 注意cleaned_data裡面是unicode~
		if self.cleaned_data['Cakeflavor'] == u'原味':
			return 500
		if self.cleaned_data['Cakeflavor'] == u'抹茶紅豆':
			return 550
		if self.cleaned_data['Cakeflavor'] == u'芝麻':
			return 500
		if self.cleaned_data['Cakeflavor'] == u'蔓越莓':
			return 650
			

class Customer_infoForm(forms.Form):

	Customer_name = forms.CharField(max_length=20,label='您的姓名')
	Address =  forms.CharField(max_length=200,label='您的地址(或方便的面交地點)')
	Phonenumber = forms.CharField(max_length=20,label='您的聯絡電話')
	Email = forms.EmailField(max_length=100,label='您的Email(非必填)',required=False)
	Catchmethod = forms.ChoiceField(label='取貨方式(面交只限新竹市區)',choices= (
		('郵寄','郵寄'),
		('面交','面交'),
	    
	))
	Catchlocation = forms.ChoiceField(label='取貨地點(面交者才需要填寫)',required=False,choices= (
		('',''),
		('新竹聖教會','A(新竹聖教會)'),
		('城隍廟','B(城隍廟)'),
		('棒球場','C(棒球場)'),
		('江山藝改所','D(江山藝改所)'),
		('新竹市政府','E(新竹市政府)'),
	    
	))

	def sendmail(self,Buy_infos):
		send_mail(
		self.cleaned_data['Customer_name']+'先生/小姐，您的訂單', 
		'以下是您訂購的商品:\n'+
		'\n'.join(self.merge_str(Buy_infos))+'\n感謝您的訂購!!!'
		, 
		'h5904098@email.com', 
		[str(self.cleaned_data['Email'])],
		)

	def merge_str(self,Buy_infos):

		merge = [ 'X'.join([infos[0],str(infos[2])]) for infos in Buy_infos]
		return merge


#待解決:訂購不同數量不同種蛋糕 => 可能要用各個口味旁設置加減數量器
#Ans=>似乎做成購物車更適合
# In views.py :
# 1.利用session暫存購物車內容(設置一個加入購物車input) 
# 2.(設置一個結帳input)