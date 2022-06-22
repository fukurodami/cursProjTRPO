from cgitb import text
from tokenize import group
from turtle import title
from django.shortcuts import render
from django.views.generic.base import View
from .models import Group, Product
from .forms import OrderForm
from django.http import HttpResponse, HttpResponseRedirect

class MainView(View):
    def get(self, request):                  
        return render(request, "main.html")

class UsView(View):
    def get(self, request):                  
        return render(request, "us.html",)

class ItemsViewBedroom(View):
    def get(self, request):       
        item = Product.objects.filter(group_id=1)      
        return render(request, "bedroom.html",)

class ItemsViewLivingroom(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=2)         
        return render(request, "livingroom.html", {'item_list': item})

class ItemsViewBed(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=3)         
        return render(request, "bed.html", {'item_list': item})

class ItemsViewDresser(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=4)         
        return render(request, "dresser.html", {'item_list': item})

class ItemsViewCupboard(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=5)         
        return render(request, "cupboard.html", {'item_list': item})

class ItemsViewTable(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=6)         
        return render(request, "table.html", {'item_list': item})
    
class ItemsViewRack(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=7)         
        return render(request, "rack.html", {'item_list': item})
    
class ItemsViewHallway(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=8)         
        return render(request, "hallway.html", {'item_list': item})

class ItemsViewTeenagers(View):
    def get(self, request):    
        item = Product.objects.filter(group_id=9)         
        return render(request, "teenagers.html", {'item_list': item})

class OrderView(View):
    def get(self, request, pk):
        product = Product.objects.filter(id=pk)
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = OrderForm(request.POST)
                print(form.title)
                if form.is_valid:
                    form.save()
                    return HttpResponseRedirect('/')
            else:
                form = OrderForm()
                return render(request, "order.html", {'product': product, 'form': form})
        else:
            return render(request, "registration/login.html")

    def post(self, request, pk, user):
        product = Product.objects.filter(id=pk)
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = OrderForm(request.POST)
                if form.is_valid:
                    forma = form.save(commit=False)
                    forma.user = user.username
                    forma.product = product
                    forma.save()
                    return HttpResponseRedirect('/')
            else:
                form = OrderForm()
                return render(request, "order.html", {'product': product, 'form': form})
        else:
            return render(request, "registration/login.html")
