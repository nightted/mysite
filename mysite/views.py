from django.shortcuts import render ,render_to_response
from django.http import HttpResponse, HttpResponseRedirect   
from datetime import datetime
from cheesecake.models import Cake

from django.conf.urls.static import static
from django.conf import settings





def welcome(request):
	
    if 'user_name' in  request.GET:

        if not request.GET['user_name']  :
        	return HttpResponseRedirect('/welcome/')

        else:
        	post_list = Post.objects.all()
    	return render(request, 'home.html',locals())

    else:
       	return render(request,'welcome.html', locals())