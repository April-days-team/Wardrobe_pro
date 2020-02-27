from datetime import time

from django.shortcuts import render

# Create your views here.
from daogouapp.models import SaleStore


# 卖家
def sale_view(request):
    sales = SaleStore.objects.all()
    return render(request,'daogouapp/sale.html',locals())


# 增加商家
def add_sale_view(request):
    if request.method == 'GET':
        sales = SaleStore.objects.all()
        return render(request,'daogouapp/add_store.html')
    elif request.method == 'POST':
        store_name = request.POST.get('store_name','')
        store_num = request.POST.get('store_num','')
        create_time = time.time()
        new_sale = SaleStore.objects.create(store_name=store_name,store_num=store_num,create_time=create_time)




