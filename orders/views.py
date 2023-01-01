from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem
from django.contrib import messages


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'نمی توانید به صفحه خرید بروید چون سبد خرید شما خالی می باشد ')
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST, )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )

            cart.clear()
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            messages.success(request, 'عملیات خرید با موفقیت انجام شد  ')

    return render(request, 'orders/order_create.html',
                  {
                      'form': order_form,
                   })
