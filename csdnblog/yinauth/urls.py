from django.urls import path
from .import views


app_name = 'yinauth'
urlpatterns = [
    path('login', views.yinlogin, name='login'),
    path('logout', views.yinlogout, name='logout'),
    path('register', views.register, name='register'),
    path('email/captcha',views.send_email, name='email_captcha'),

]