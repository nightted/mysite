# -*- coding: UTF-8 -*-
from django import forms


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
	Address =  forms.CharField(max_length=200,label='您的地址')
	Phonenumber = forms.CharField(max_length=20,label='您的聯絡電話')
	Email = forms.EmailField(max_length=100,label='您的Email(非必填)',required=False)

#待解決:訂購不同數量不同種蛋糕 => 可能要用各個口味旁設置加減數量器
#Ans=>似乎做成購物車更適合
# In views.py :
# 1.利用session暫存購物車內容(設置一個加入購物車input) 
# 2.(設置一個結帳input)