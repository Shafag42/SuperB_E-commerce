from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView
from .models import Faq
from blog.models import Post
from product.models import product_version
from .forms import ContactUsForm, ContactInfoForm

class HomePage(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by("-created_at").all()[:2]

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['items'] = product_version.objects.all()
        context['featured_items'] = product_version.objects.all()
        context['best_items'] = product_version.objects.all()
        context['new_items'] = product_version.objects.all()
        return context

class ContactUs(CreateView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your comment has been sent successfully!')
        return redirect('contact_us')

class ContactInfo(CreateView):
    template_name = 'contact_information.html'
    form_class = ContactInfoForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your comment has been sent successfully!')
        return redirect('contact_information')

class FAQ(ListView):
    template_name = 'faq.html'
    model = Faq
    context_object_name = 'faqs'


def error(request):
    return render(request, '404error.html')

def about_us(request):
    return render(request, 'about_us.html')


