
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Product
from cart.models import Cart
from address.models import Add
from django.utils.datastructures import MultiValueDictKeyError

def home(request):
    products=Product.objects


    return render(request,'products/home.html',{'products':products})
def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)

    return render(request,'products/detail.html',{'product':product})
def catagory(request,catagory_id):
    if catagory_id==0:
        products=Product.objects
        return render(request,'products/home.html',{'products':products})
    else:

        products=Product.objects.filter(field=catagory_id)
        return render(request,'products/catagory.html',{'products':products})
@login_required
def addcart(request,product_id):
    current=request.user
    a=0
    user=str(current)
    cart=get_object_or_404(Cart,user=user)
    item=cart.cartitem
    for i in range(1,len(item)):
        if item[i][0]==product_id:
            a=1
    if a==0:
        cart.cartitem=cart.cartitem+[[product_id]]
    cart.save()
    return redirect('/products/'+str(product_id))
    #return render(request,'products/detail.html',{'product':product})

@login_required
def viewcart(request):
    current=request.user
    user=str(current)
    cart=get_object_or_404(Cart,user=user)
    item=cart.cartitem
    sum =0


    id=()
    i=0
    for i in range(1,len(item)):
        ob=get_object_or_404(Product,pk=item[i][0])
        print(ob.price)
        sum=sum+ob.price
        it=()
        it=(item[i][0],)
        id=(id+it)


    products=Product.objects.filter(id__in=id)


    cart.save()
    return render(request,'products/viewcart.html',{'product':products,'no':i,'sum':sum})
@login_required
def address(request):
    current=request.user
    user=str(current)
    cart=get_object_or_404(Add,uname=user)

    try:


            cart.fname=request.POST['firstName']
            cart.lname=request.POST['lastName']
            cart.email=request.POST['email']
            cart.address1=request.POST['address']
            cart.address2=request.POST['address2']
            cart.country=request.POST['country']
            cart.state=request.POST['state']
            cart.zip=request.POST['zip']
            cart.save()
            return render(request,'products/viewcart.html')
    except:

            return render(request,'products/address.html')
