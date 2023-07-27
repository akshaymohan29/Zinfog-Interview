from django.urls import path
from  .views import home,add_to_cart,remove_from_cart,checkout


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
]