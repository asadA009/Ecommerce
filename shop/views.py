from shop.models import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil, prod

def index(request):
   # products=product.objects.all()
  #  print(products)
 #   n=len(products)
#    nSlides = n//4 + ceil((n/4)-(n//4))
    allProds=[]
    catprods= product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for item in cats:
        prod=product.objects.filter(category=item)

        n=len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    #allProds=[[products,range(1,nSlides) ,nSlides],
             # [products,range(1,nSlides) ,nSlides]]
    params={'allProds':allProds}
    return render(request, 'shop/index.html', params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("We are contact")
def tracker(request):
    return HttpResponse("We are tracker")
def search(request):
    return HttpResponse("We are search")
def productview(request):
    return HttpResponse("We are productview")
def checkout(request):
    return HttpResponse("We are checkout")
    