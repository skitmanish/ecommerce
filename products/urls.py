
from django.urls import path
from . import views

urlpatterns = [

            path('<int:product_id>',views.detail,name='detail'),
            path('<int:product_id>/addcart',views.addcart,name='addcart'),
            path('viewcart/',views.viewcart,name='viewcart'),
            path('address/',views.address,name='address'),




]
