#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include,url
from django.contrib import admin
from  cheesecake.views  import home,CommentFormView,BuyFormView,CartCountView,SuccessView

from views import  welcome




urlpatterns = [
    #主頁用
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    #買東西用
    url(r'^Buy/$', BuyFormView.as_view(),name='Buy'),
    url(r'^CartCount/$', CartCountView.as_view(),name='CartCount'),
    url(r'^Success/$', SuccessView.as_view(),name='Success'),
    #給評價用
    url(r'^Comment/$', CommentFormView.as_view(),name='Comment'),
    #沒用
    url(r'^welcome/$', welcome),
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()