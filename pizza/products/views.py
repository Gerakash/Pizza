# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import Product,AboutUs
from .form import*
# Create your views here.
from .filters import ProductFilter
#jinja
from .tokens import account_activation_token


def homepage(request):
    products = Product.objects.all()
    filters = ProductFilter(request.GET,queryset=products)
    products = filters.qs
    return render(request,'products/products.html',{"products":products, "filters":filters})


def aboutus_page(request):
    abouts = AboutUs.objects.all()
    return render(request,'products/aboutus.html',{"abouts":abouts})

# def contacts(request):
#     contacts = Contact.objects.all()
#     return render(request,'products/contacts.html',{"contacts":contacts})

def register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            Profile.objects.create(user=user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('products/acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email,]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    return render(request,'products/register.html', {'form': form})



def user_list(request):
    users = Profile.objects.get(user=request.user)
    context = {'users': users}
    return render(request, 'products/user.html', context)


def create_order(request, product_id):
    user1 = Profile.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    total_price = 0
    form = OrderForm(initial={'product':product,'user':request.user})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = product.price * form.cleaned_data['quantity']
            form.save()
            if form.cleaned_data['payment_type'] == 'Wall':
                if user1.wallet >= total_price:
                    user1.wallet -= total_price
                    return HttpResponse('Thank you for shopping!')
                else:
                    return HttpResponse('payment!')
            else:
                user1.order_count += 1
                user1.save()
    context = {'form':form, 'total_price':total_price}
    return render(request,'products/create_order.html',context)


def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'products/create_order.html',context)


def delete_order(request,order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context = { 'order':order}
    return render(request,'products/delete.html',context)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse ('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')





