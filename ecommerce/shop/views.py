from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404

from shop.models import category, product


# Create your views here.
def allprodcat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        products_list=product.objects.all().filter(category_name=c_page,available=True)
    else:
        products_list=product.objects.all().filter(available=True)

    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products})

def prodetail(request,c_slug,product_slug):
    try:
        products=product.objects.get(category_name__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':products})
