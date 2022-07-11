from django.shortcuts import render

# Create your views here.
from shopconfigapp.models import ShopItem


def shop_main(request):

    print('alidfjalisjdfliajsdfijasdf')
    context = {}
    context['test'] = 'get_item'
    context['self_ph'] = ShopItem.objects.filter(ca_id=10)
    context['case_film'] = ShopItem.objects.filter(ca_id=20)
    return render(request, 'shop/shopmain.html', context)


def shop_item(request, id):
    context = {}
    get_item = ShopItem.objects.get(it_id=id)
    context['get_item'] = get_item
    th_img_list = []
    img_list = []
    img_count = []
    for i in range (1,10):
        chk_img_url = getattr(get_item, f'it_img{i}')
        if chk_img_url:

            img_count.append(i)
            img_list.append(chk_img_url.url)
            th_img_list.append(chk_img_url.url)

    context['img_list'] = zip(img_count, img_list)
    context['th_img_list'] = th_img_list
    context['test'] = 'ooooooooo'
    return render(request, f'shop/itemskin/{get_item.it_skin}', context)


def shop_cart(request):
    return render(request, 'shop/shop_cart.html', )


def shop_order(request):
    return render(request, 'shop/shop_order.html', )


def ph_order(request):
    return render(request, 'shop/ph_order.html', )
