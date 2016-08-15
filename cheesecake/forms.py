from django import forms

class CommentForm (forms.Form):
	user = forms.CharField(max_length = 20)
	email = forms.EmailField(max_length = 20,required= False)
	content = forms.CharField(max_length=500)

