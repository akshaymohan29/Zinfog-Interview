from django.urls import path
from  .views import userlogin,hello,signup


urlpatterns = [
    # path('admin/', admin.site.urls), 
    path('login',userlogin,name='login'),
    path('hello',hello,name='hello'),
    path('signup', signup, name='signup'),

]