from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Cart

from .forms import CartForm

def creat_form_view(request):
    my_form = CartForm(request.POST or None)
    
    if my_form.is_valid():
        my_form.save()
        my_form = CartForm()
    context = {
        'form': my_form,
        'my_txt': '<h1>Alhamdoulillah</h1>'
    }
    return render(request, 'create_form.html', context)


def cart_detail_view(request, id):
    obj = Cart.objects.get(id=id)

    obj1 = get_object_or_404(Cart, id=id)
    if request.method == "POST":
        obj.delete()
        redirect('../product/list')

    context = {
        'object': obj,
        'object1': obj1
    }
    return render(request, 'cart_detail.html', context)


def cart_list_item(request):
    queryset = Cart.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, 'item_list.html', context)



