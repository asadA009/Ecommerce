from shop.models import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from .models import Contact
from math import ceil
from math import prod

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
    if(request.method)=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        description=request.POST.get('description','')
        contact = Contact(name=name, email=email, phone=phone, description=description)
        contact.save()

    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def productview(request,id):
    products=product.objects.filter(id=id)
    return render(request,'shop/prodview.html', {'products':products[0]})
def checkout(request):
    return render(request,'shop/checkout.html')
    