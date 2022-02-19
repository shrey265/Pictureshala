from unicodedata import name
from home import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('post',views.post,name='post'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('details',views.details,name='details'),
    path('picture_detail/<slug>',views.picture_detail,name='picture_detail'),
    path('see_pics/',views.see_pics,name='see_pics'),
    path('pic_delete/<id>',views.pic_delete,name='pic_delete'),
    
    path('logout',views.logout_view,name='logout_view'),
    path('verify/<token>',views.verify,name='verify'),
    path('success',views.success,name='success'),
  
]