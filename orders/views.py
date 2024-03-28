from django.shortcuts import render, redirect
from accounts.models import UserProfile
from cart.models import CartItem
from store.models import Product
from .forms import OrderForm
import datetime
from .models import Order, OrderProduct
from django.contrib.auth.decorators import login_required


def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_cnt = cart_items.count()
    if cart_cnt <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    grand_total = total + tax

    shipping_address = UserProfile.objects.get(user=current_user)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
            data = form.save(commit=False)
            data.user = current_user
            data.shipping_address = shipping_address
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number

            
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            if data.payment_method == 'Stripe':
                context = {
                    'order': order,
                    'cart_items': cart_items,
                    'total': total,
                    'tax': tax,
                    'grand_total': grand_total,
                    'shipping_address': shipping_address,
                }
                return render(request, 'orders/payments.html', context)
            elif data.payment_method == 'COD':
                order.payment_method = 'COD'
                order.is_ordered = True
                order.save()
                cart_items = CartItem.objects.filter(user=request.user)

                for item in cart_items:
                    orderproduct = OrderProduct()
                    orderproduct.order_id = order.id
                    orderproduct.user_id = request.user.id
                    orderproduct.product_id = item.product_id
                    orderproduct.quantity = item.quantity
                    orderproduct.product_price = item.product.price
                    orderproduct.ordered = True
                    orderproduct.save()

                    cart_item = CartItem.objects.get(id=item.id)
                    product_variation = cart_item.variations.all()
                    orderproduct = OrderProduct.objects.get(id=orderproduct.id)
                    orderproduct.variations.set(product_variation)
                    orderproduct.save()


                    # Reduce the quantity of the sold products
                    product = Product.objects.get(id=item.product_id)
                    product.stock -= item.quantity
                    product.save()


                # Continue to order complete view for Cash on Delivery
                CartItem.objects.filter(user=current_user).delete()
                return redirect('order_complete')
        else:
            return redirect('checkout')

def payments(request):
    
    return render(request, 'orders/payments.html')

@login_required(login_url='login')
def order_complete(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity

    context = {
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal,
    }
    return render(request, 'orders/order_complete.html', context)