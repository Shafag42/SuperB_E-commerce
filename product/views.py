from itertools import count
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView
from .models import product, product_version,Manufacturer,Color,Size, category, reviews,product_images
from .forms import ReviewForm
from django.http import HttpResponseForbidden
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import  reverse
from django.core.paginator import Paginator
from .forms import ReviewForm

class Productview(DetailView,CreateView):
    model = product
    pk_url_kwarg = 'pk'
    template_name= "product-detail.html"
    context_object_name= "product"
    form_class = ReviewForm


    def form_valid(self,form,*args, **kwargs):
        form.instance.product_id=product_version.objects.get(pk=self.kwargs.get("pk"))
        form.instance.save()
        return redirect('product_detail', pk=self.kwargs.get("pk"))

    # def post(self, request, *args, **kwargs):

    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)  
    #         review.product_id = product_version.objects.get(pk=self.kwargs.get("pk"))
    #         review.save()
    #         # product = product_version.objects.get(pk=self.kwargs.get("pk"))
    #         # product.review_sayi += 1  # type: ignore
    #         # product.save()
    #     return redirect('product_detail', pk=self.kwargs.get("pk"))


    def get_object(self, queryset=None):
        return product_version.objects.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context= super(Productview,self).get_context_data(**kwargs)
        context["related_products"] = product_version.objects.all()
        context["product_upsells"] = product_version.objects.all()
        context["product_images"] = product_images.objects.filter(product_id=self.object)   # type: ignore
        context['reviews'] = reviews.objects.all()  
        return context



def review_sayi(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else: 
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'product-list.html', context)


    

class Product_list(ListView):
    model = product_version
    template_name= "product-list.html"
    context_object_name= "product_lists"
    form_class = ReviewForm
    paginate_by = 1

    def get_queryset(self):  # sourcery skip: use-named-expression
        color=self.request.GET.get('color')
        size=self.request.GET.get('size')
        manufacturer=self.request.GET.get('manufacturer')

        if color:
            self.queryset = product_version.objects.filter(color__name=color).all()

        elif size:
            self.queryset = product_version.objects.filter(size__name=size).all()
        
        elif manufacturer:
            self.queryset = product.objects.filter(manufacturer__name=manufacturer).all()
        else:
            self.queryset = product_version.objects.all()

        return self.queryset

    

    def get_context_data(self, **kwargs):
        context= super(Product_list,self).get_context_data(**kwargs)
        context["category_list"] = category.objects.all()
        context["Manufacturers"] = product.objects.values_list("manufacturer__name", flat=True).distinct().values('manufacturer__name').annotate(count = Count('manufacturer__name')) 
        context["Colors"] = product_version.objects.values_list("color__name", flat=True).distinct().values('color__name').annotate(count = Count('color__name'))
        context["Sizes"] = product_version.objects.values_list("size__name", flat=True).distinct().values('size__name').annotate(count = Count('size__name'))
        return context

    

       
    
    
