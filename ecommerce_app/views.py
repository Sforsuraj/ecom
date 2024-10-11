from django.shortcuts import render,redirect
from .models import shop,shop_detail,shop_cart,category,billing_address,shipping_address
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import registeruser
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
@login_required
def home(request):
    prod=shop.objects.all()
    cat=category.objects.all()
    cat1=category.objects.all()
    data={"prod":prod,"cat1":cat1,"cat":cat}
    return render(request,'index.html',data)

def category_view(request,id):
    prod=shop.objects.filter(category_id=id)
    cat1=category.objects.all()
    data={"prod":prod,"cat1":cat1}
    return render(request,'shop.html',data)

@login_required
def shop_view(request):
    prod=shop.objects.all()
    cat1=category.objects.all()
    data={"prod":prod,"cat1":cat1}
    return render(request,'shop.html',data)

@login_required
def checkout(request):
    sub_total=0
    total=0
    shipping=0
    user_id=request.user.id
    d=shop_cart.objects.filter(user_id_id=user_id)
    for i in d:
        sub_total+=i.product_quantity*i.product_id.product_price
    total=sub_total+int(sub_total*.02)
    shipping=int(sub_total*.02)
    cat1=category.objects.all()
    try:
        b=billing_address.objects.get(user_id_id=request.user.id)
        if b != None:
            data={"d":d,"sub_total":sub_total,"total":total,"shipping":shipping,"cat1":cat1,"bill":b}
            return render(request,'checkout.html',data)
    except:
        pass
    data={"d":d,"sub_total":sub_total,"total":total,"shipping":shipping,"cat1":cat1}
    return render(request,'checkout.html',data)


@login_required
def cart(request):
    sub_total=0
    total=0
    shipping=0
    user_id=request.user.id
    d=shop_cart.objects.filter(user_id_id=user_id)
    for i in d:
        sub_total+=i.product_quantity*i.product_id.product_price
    total=sub_total+int(sub_total*.02)
    shipping=int(sub_total*.02)
    cat1=category.objects.all()
    data={"d":d,"sub_total":sub_total,"total":total,"shipping":shipping,"cat1":cat1}
    return render(request,'cart.html',data)


@login_required
def contact(request):
    cat1=category.objects.all()
    if request.method=="POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email'), ]
        try:
            #send_mail( subject, message, email_from, recipient_list )
            data={"title":"contact","msg":'message send successfully!',"mode":"success","cat1":cat1}
            return render(request,'contact.html',data)
        except BadHeaderError:
            data={"title":"contact","msg":'message not send !',"mode":"danger","cat1":cat1}
            return render(request,'contact.html',data)
    data={"title":"contact","msg":'',"cat1":cat1}
    return render(request,'contact.html',data)

@login_required
def detail(request,id):
    p=shop.objects.all()
    cat1=category.objects.all()
    prod=shop.objects.get(id=id)
    prod_d=shop_detail.objects.get(product_id=id)
    data={"prod":prod,"prod_d":prod_d,"p":p,"cat1":cat1}
    return render(request,'detail.html',data)

def sign_in(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'account/sign_in.html')
    return render(request,'account/sign_in.html')

def sign_up(request):
    form=registeruser()
    if request.method=="POST":
        form=registeruser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    return render(request,'account/sign_up.html')


@login_required
def logout_u(request):
    logout(request)
    return redirect('login')

@login_required
def add_cart(request,id1,id2):
    if request.method=="POST":
        user_id=id1
        product_id=id2
        product_size=request.POST.get('product_size')
        product_color=request.POST.get('product_color')
        product_quantity=request.POST.get('product_quantity')
        try:
            cart=shop_cart.objects.get(user_id_id=user_id,product_id_id=product_id,product_size=product_size,product_colour=product_color)
            cart.product_quantity=int(cart.product_quantity)+int(product_quantity)
            cart.save()
            return redirect('cart')
        except:
            cart=shop_cart(user_id_id=user_id,product_id_id=product_id,product_size=product_size,product_colour=product_color,product_quantity=product_quantity)
            cart.save()
            return redirect('cart')
        
    return render(request,'cart.html')

@login_required
def remove_cart(request,id1,id2,size,colour):
    if request.method == 'POST':
        try:
            d=shop_cart.objects.get(user_id_id=id1,product_id_id=id2,product_size=size,product_colour=colour)
            d.delete()
            return redirect('cart')
        except:
            pass
    return redirect('cart')

@login_required
def update_cart(request,id1,id2,size,colour):
    user_id=id1
    product_id=id2
    if request.method=="POST":
        try:
            prod=shop_cart.objects.get(user_id_id=user_id,product_id_id=product_id,product_size=size,product_colour=colour)
            prod.product_quantity=request.POST.get("product_quantity")
            prod.save()
            return redirect('cart')
        except:
            pass
    return redirect('cart')
        
        

def billing(request,id):
    try:
        b=billing_address.objects.get(user_id_id=id)
        if b!=None:
            if request.method=="POST":
                b.user_id_id=id
                b.first_name=request.POST.get("first_name")
                b.last_name=request.POST.get("last_name")
                b.email=request.POST.get("email")
                b.phone=request.POST.get("phone")
                b.address_1=request.POST.get("address_1")
                b.address_2=request.POST.get("address_2")
                b.country=request.POST.get("country")
                b.city=request.POST.get("city")
                b.state=request.POST.get("state")
                b.zip_code=request.POST.get("zip_code")
                b.save()
    except:
        if request.method=="POST":
            user_id=id
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            address_1=request.POST.get("address_1")
            address_2=request.POST.get("address_2")
            country=request.POST.get("country")
            city=request.POST.get("city")
            state=request.POST.get("state")
            zip_code=request.POST.get("zip_code")
            bill=billing_address(user_id_id=user_id,first_name=first_name,last_name=last_name,email=email,phone=phone,address_1=address_1,address_2=address_2,country=country,city=city,state=state,zip_code=zip_code)
            bill.save()
            return redirect('checkout')
        
    
    return redirect('checkout')

