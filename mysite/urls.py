from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include,url
from django.contrib import admin
from  cheesecake.views  import home,CommentFormView,BuyFormView

from views import  welcome




urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^Buy/$', BuyFormView.as_view(),name='Buy'),
    url(r'^Comment/$', CommentFormView.as_view(),name='Comment'),

    url(r'^welcome/$', welcome),
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()