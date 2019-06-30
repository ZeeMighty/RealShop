from django.http import HttpResponse
from django.template import loader
from HiPage.models import Good, Size, Good_Get, UserGood
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import GoodGet
from django.views.generic import View
from django.contrib import auth
from django.views.decorators import csrf
#from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login

def IndexView(request):
    return render(request, 'HiPage/homepage.html', {'username': auth.get_user(request).username})

def Men(request):
    good = Good.objects.all()
    return render(request, 'HiPage/men.html', context = {'SIZE': good})

class Adding(View):
    def get(self, request, good_id):
        good = Good.objects.filter(id = good_id)
        good1 = Good.objects.get(id = good_id)
        form = GoodGet(initial = {'Name': good1.Name, 'Price': good1.Price}, good_id1 = good_id)
        return render(request, 'HiPage/add_to_cart.html', context = {'form': form, 'good': good})

    def post(self, request, good_id):
        good1 = Good.objects.get(id = good_id)
        form = GoodGet(request.POST, initial = {'Name': good1.Name, 'Price': good1.Price}, good_id1 = good_id)
        if form.is_valid():
            form.save()
            return redirect('/men')
        good = Good.objects.filter(good_id1 = good_id)
        return render(request, 'HiPage/add_to_cart.html', context = {'form': form, 'good': good})

def Cart(request):
#    goods = Good_Get.objects.all()
    goods = UserGood.objects.all()
    return render(request, 'HiPage/cart.html', context = {'good': goods})

def delete(request, good_id):
        #Good_Get.objects.get(id = good_id).delete()
        UserGood.objects.get(id = good_id).delete()
        return HttpResponseRedirect("/cart")



def Login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        print(user, username, password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'HiPage/Login.html', args)

    else:
        return render(request, 'HiPage/Login.html', args)

def Logout(request):
    auth.logout(request)
    return redirect('/')



def AboutUs(request):
    return render(request, 'HiPage/AboutUs.html')

def Terms(request):
    return render(request, 'HiPage/Terms.html')

def Delivery(request):
    return render(request, 'HiPage/Delivery.html')

def Refund(request):
    return render(request, 'HiPage/Refund.html')

def Support(request):
    return render(request, 'HiPage/Support.html')
