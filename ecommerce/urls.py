 
from django.contrib import admin
from django.urls import path , include
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    #Admin urls
    
    path('', include('store.urls')) ,   #store urls
    
    path('cart/', include('cart.urls')), #cart urls
    
    path('account/', include('account.urls')), #Account app urls
    
    path('payment/', include('payment.urls')),
]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)