from django.shortcuts import render
from .models import Items,SurfItem,Transaction
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def home(req):
    
    req.session['cart']={}
    # print(dict(req.session))
    return render(req,"product/index.html")


def allitems(req):
    if req.method=="POST":
        stock=int(req.POST.get('instock'))
        required=int(req.POST.get('req_quan'))
        id=int(req.POST.get('id_product'))
        print(type(stock))
        print(required)
        if required > stock:
            data=Items.objects.all()
            return render(req,'product/allitems.html',{'data':data,'msg1':'INAPROPRIATE CHOICE','id':id})
        cat="allitems"
        cat_id=cat+" "+str(id)
        cart=req.session.get('cart')        #Local Variable
        print(cart)
        old=cart.get(cat_id)
        print(old)
        if old:
            cart[cat_id]=required+old
        else:
            cart[cat_id]=required
        print(cart)
        req.session['cart']=cart        # Assign new value to the cart
    data=Items.objects.all()
    return render(req,"product/allitems.html",{'data':data})


def surf(req):
    if req.method=="POST":
        stock=int(req.POST.get('instock'))
        required=int(req.POST.get('req_quan'))
        id=int(req.POST.get('id_product'))
        print(type(stock))
        print(required)
        if required > stock:
            data=SurfItem.objects.all()
            return render(req,'product/allitems.html',{'data':data,'msg1':'INAPROPRIATE CHOICE','id':id})
        cat="surf"
        cat_id=cat+" "+str(id)
        cart=req.session.get('cart')
        old=cart.get(cat_id)
        print(cart)
        if old:
            cart[cat_id]=required+old
        else:
            cart[cat_id]=required
        print(cart)
        req.session['cart']=cart
    data=SurfItem.objects.all()
    return render(req,"product/allitems.html",{'data':data})

def search(req):
    srch=req.POST.get('search')
    results = Items.objects.filter(name__contains=srch)
    results2 = SurfItem.objects.filter(name__contains=srch)
    if  results or results2:
        return render(req,"product/search.html",{'result':results})

def mycart(req):
    data=req.session.get("cart")
    list_final=[]
    GT=0
    for i,j in data.items():
        if "allitems" in i:
            id=int(i[9:])
            d1=Items.objects.get(pk=id)
            price=d1.price
            total= j*price
            lis=[d1,j,total]
            list_final.append(lis)
            GT+=total

        if "surf" in i:
            id=int(i[5:])
            d1=SurfItem.objects.get(pk=id)
            price=d1.price
            total= j*price
            lis=[d1,j,total]
            list_final.append(lis)
            GT+=total


    return render(req,"product/mycart.html",{"list_final":list_final,"GT":GT})

def make_payment(req):
    
    if req.method=="POST":
        if req.user.is_authenticated:
            data=req.session.get('cart')
            for i,j in data.itams():
                if 'soap' in i:
                    cat='soap'
                    id=int(i[4:])
                    quan=j
                    Transaction(user=user)

            return HttpResponse('plese procede for payment')
        else:
            return HttpResponseRedirect("/auth1/login/")