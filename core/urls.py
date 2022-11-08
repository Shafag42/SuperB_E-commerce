from django.urls import path
from .views import error, about_us, ContactInfo, ContactUs, FAQ,HomePage
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('404error/', error, name='404error'),
    path('about_us/', about_us, name='about_us'),
    path('contact_information/', ContactInfo.as_view(), name='contact_information'),
    path('contact_us/', ContactUs.as_view(), name='contact_us'),
    path('faq/', FAQ.as_view(), name= 'faq'),  
    path('', HomePage.as_view(), name='index')
    ]
