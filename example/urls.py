
from django.contrib import admin
from django.urls import path,include
from products import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('catagory/<int:catagory_id>/',views.catagory,name='catagory'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
