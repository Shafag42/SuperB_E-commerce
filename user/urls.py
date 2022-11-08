
from django.urls import path,include

from django.contrib.auth import views as auth_views #import this
from django.contrib.auth.views import LogoutView
from .views import account_informatin,address_book,change_password,login_view,RegisterView, activate,LogInView,ResetPasswordView, ResetPasswordConfirmView
urlpatterns = [
   
    path('account_information/', account_informatin, name='account_information'),
    path('address_book/', address_book,name='address_book'),
    path('change_password/', change_password, name= 'change_password'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), #yoxla logout.html

    #path('password_reset_done/',password_reset_done,name='password_reset_done'),
    # path('password_reset_confirm/<str:uidb64>/<str:token>/',
    #     ResetPasswordConfirmView.as_view(),
    #     name='password_reset_confirm'),
    #path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'), 
    path("password_reset", ResetPasswordView.as_view(), name="password_reset"),
    path('confirmation/<str:uidb64>/<str:token>/', activate ,name='confirmation'),

]