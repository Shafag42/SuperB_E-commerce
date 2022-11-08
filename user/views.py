from .models import *
from .forms import UserRegisterForm, LoginForm,ResetPasswordForm,CustomSetPasswordForm, ChangePasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.utils.encoding import force_bytes,force_str
from django.contrib import messages #import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, BadHeaderError
from .tokens import account_activation_token

from django.contrib.auth.views import LoginView, PasswordResetView

from django.shortcuts import render,redirect
from .forms import UserRegisterForm,LoginForm ,Account_InformationForm
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from SuperB_Wolves.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    template_name='register.html'
    form_class=UserRegisterForm
    success_url=reverse_lazy('login')

    def post(self,request,*args,**kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.is_active = False
            User.save()

            subject = "Activate Your Account"
            current_site = get_current_site(request)
            messages = render_to_string("confirmation_email.html",{
                "User" : User ,
                "domain": current_site.domain,
                "uid" : urlsafe_base64_encode(force_bytes(User.pk)),
                "token" : account_activation_token.make_token(User)

            })

            from_email = EMAIL_HOST_USER
            to_email = request.POST['email']
            send_mail(subject,messages,from_email,[to_email, ])

            return(redirect("/"))
        return render(request, self.template_name, {'form': form})

class LogInView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class ResetPasswordView(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = ResetPasswordForm
    email_template_name= 'password_reset_email.html'
    subject_template_name = 'reset_password_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      "If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password_reset_done')

    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(ResetPasswordView, self).get_success_url()


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='password_reset_confirm.html',   # type: ignore
    form_class=CustomSetPasswordForm,  # type: ignore
    success_url = reverse_lazy('password_reset_complete')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(ResetPasswordConfirmView, self).get_success_url()


       

def activate(request,uidb64,token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active = False).first()

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("/")


def account_informatin(request):  # sourcery skip: instance-method-first-arg-name
    if request.method=="POST":
        form=Account_InformationForm(request.POST)
        if form.is_valid(): 
            form.save()
    else:
        form= Account_InformationForm()
    context = {
        'form' : form
    }
    return render(request,'account_information.html', context)


def address_book(request):
    
    return render(request,'address_book.html')


def change_password(request):
    return render(request,'change_password.html')


def login_view(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if user is not None:
                login(request, user)
                return redirect('index')
            
    else:
        form = LoginForm()

    context ={
        "form": form
    }

    return render(request, 'login.html', context)
   
def register(request):   #sourcery skip: last-if-guard
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserRegisterForm()
    context={
        "form" : form   
         }
    return render(request,'register.html',context)