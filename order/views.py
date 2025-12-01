from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from .forms import OrderForm
from django.views import View
from .models import *

# Create your views here.
class OrderView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, "order/submit.html", {"form": form})
    
    def post(self, request):
        form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "order/submit.html", {"form": form})
    
def thank_you(request):
    return render(request, "order/thank_you.html")

def order_list(request):
    orders = Order.objects.all().order_by('pickup')
    context = {
        "orders": orders
    }
    return render(request, "order/order_list.html", context)


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order:order_list")
    else:
        form = OrderForm(instance=order)

    context = {
        "form": form,
        "order": order,
    }
    return render(request, "order/order_edit.html", context)

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        order.delete()
        return redirect("order:order_list")

    context = {"order": order}
    return render(request, "order/order_confirm_delete.html", context)