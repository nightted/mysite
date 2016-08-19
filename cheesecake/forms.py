# -*- coding: UTF-8 -*-
from django import forms

class CommentForm (forms.Form):
	
	Nickname = forms.CharField(max_length=20,label='您的暱稱')
	Email = forms.EmailField(max_length=100,label='您的Email(非必填)',required=False)
	Cakeflavor= forms.CharField(max_length=20,label='您訂購的口味')
	Content = forms.CharField(max_length = 500 ,label='您的評論')




class BuyFrom(forms.Form):

	Customer_name = forms.CharField(max_length=20,label='您的姓名')
	Address =  forms.CharField(max_length=200,label='您的地址')
	Phonenumber = forms.CharField(max_length=20,label='您的聯絡電話')
	Email = forms.EmailField(max_length=100,label='您的Email(非必填)',required=False)
	Cakeflavor = forms.CharField(max_length=20,label='您訂購的口味')
	Number = forms.IntegerField(label='您訂購的數量')

	#待解決:訂購不同數量不同種蛋糕 => 可能要用各個口味旁設置加減數量器