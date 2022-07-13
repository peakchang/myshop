import datetime
import os
import random
from pathlib import Path
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import json
# Create your views here.
from django import forms
from django.urls import reverse

from shopconfigapp.models import ShopConfig
from shopconfigapp.forms import EditorForm, QuillFieldForm
from shopconfigapp.models import ShopCategory, ShopItem
import shop



def item_form(request):
    context = {}

    if request.method == "POST":
        get_id = request.POST.get('it_id')
        if request.POST.get('act_val') == 'insert':
            shop_item = ShopItem()
            shop_item.it_id = get_id
        else:
            shop_item = ShopItem.objects.get(it_id=get_id)

        get_checked = request.POST.get('it_use')
        if get_checked is None:
            get_checked = 'False'
        shop_item.it_use = get_checked

        get_checked = request.POST.get('it_main_item')
        if get_checked is None:
            get_checked = 'False'
        shop_item.it_main_item = get_checked

        get_list = ['ca_id', 'ca_id2', 'ca_id3', 'it_skin', 'it_name', 'it_sub_name', 'it_depend_item',
                    'it_co_type', 'it_info', 'it_cust_price', 'it_price', 'it_option', 'it_naver_category',
                    'it_color', 'it_color_code']
        for get in get_list:
            if request.POST.get(f'{get}'):
                setattr(shop_item, get, request.POST.get(get))

        tong_list = ['sk', 'kt', 'lg']
        for tong in tong_list:
            tong_get_list = [f'it_{tong}_fprice', f'it_{tong}_capa', f'it_{tong}_gongsi', f'it_{tong}_new_dc',
                             f'it_{tong}_mnp_g_dc', f'it_{tong}_mnp_s_dc', f'it_{tong}_gib_g_dc', f'it_{tong}_gib_s_dc']
            for tong_get in tong_get_list:
                if request.POST.get(f'{tong_get}'):
                    setattr(shop_item, tong_get, request.POST.get(tong_get))

        # 이미지 저장
        for i in range(1, 10):
            temp_name = f'it_img{i}'
            pre_img = getattr(shop_item, temp_name)
            new_img = request.FILES.get(temp_name)
            if pre_img and new_img:
                os.remove(pre_img.path)
                setattr(shop_item, temp_name, request.FILES.get(temp_name))
            elif not pre_img and new_img:
                setattr(shop_item, temp_name, request.FILES.get(temp_name))
            elif pre_img and not new_img:
                pass

        # 상품 설명 에디터 UP
        form = EditorForm(request.POST)
        # if form.is_valid():
        #     form.it_explain = form.cleaned_data('it_explain')
        #     form.it_explain = form.cleaned_data('it_sub_explain')

        if request.POST.get('it_explain'):
            shop_item.it_explain = request.POST.get('it_explain')
        if request.POST.get('it_sub_explain'):
            shop_item.it_sub_explain = request.POST.get('it_sub_explain')

        shop_item.save()
        return HttpResponseRedirect(reverse('shopconfig:itemlist'))

    # 메인 / 서브 상세설명 에디터 생성
    form = EditorForm()
    context['form'] = form

    # 상품코드 생성
    while True:
        result_key = make_key()
        try:
            chk_key = ShopItem.objects.get(it_id=result_key)
            if chk_key:
                result_key = make_key()
        except:
            break
    context['result_key'] = result_key

    # 최상위 분류값 가지고 오기 (하위 카테고리는 ajax로 찾기)
    category_a = ShopCategory.objects.filter(ca_rate='A')
    context['category_a'] = category_a

    # 상품 스킨 찾기 (itemskin_) 으로 시작되는 파일
    BASE_DIR = Path(__file__).resolve().parent.parent
    shop_tpl_path = f'{BASE_DIR}/shop/templates/shop/itemskin'
    file_list = os.listdir(shop_tpl_path)
    file_list_py = [file for file in file_list if file.startswith("itemskin_")]
    context['skin_list'] = file_list_py

    return render(request, 'shopconfigapp/item_form.html', context)


def item_update(request, pk):
    context = {}
    shop_item = ShopItem.objects.get(id=pk)
    context['shop_item'] = shop_item

    category_a = ShopCategory.objects.filter(ca_rate='A')
    context['category_a'] = category_a
    category_b = ShopCategory.objects.filter(ca_rate='B')
    context['category_b'] = category_b
    category_c = ShopCategory.objects.filter(ca_rate='C')
    context['category_c'] = category_c
    # 메인 / 서브 상세설명 에디터 생성
    form = EditorForm()
    quill_form = QuillFieldForm()
    context['quill_form'] = quill_form
    context['form'] = form
    context['img_range'] = range(1, 10)
    img_list = []
    img_num = []
    for i in range(1, 10):
        get_img = getattr(shop_item, f'it_img{i}')
        if get_img:
            img_list.append(get_img.url)
        else:
            img_list.append(get_img)
        img_num.append(i)
    all_img_list = zip(img_list, img_num)
    context['all_img_list'] = all_img_list
    context['img_list'] = img_list
    context['option_list'] = shop_item.it_option

    # 상품 스킨 찾기 (itemskin_) 으로 시작되는 파일
    BASE_DIR = Path(__file__).resolve().parent.parent
    shop_tpl_path = f'{BASE_DIR}/shop/templates/shop/itemskin'
    file_list = os.listdir(shop_tpl_path)
    file_list_py = [file for file in file_list if file.startswith("itemskin_")]
    context['skin_list'] = file_list_py

    # test_obj = ShopItem.objects.get(id=pk)
    # # test_img_get = test_obj.it_img1
    # test_img_get = getattr(test_obj, 'it_img1')


    return render(request, 'shopconfigapp/item_update.html', context)





def shopconfig(request):
    if request.method == 'POST':
        print(request.POST.get('test'))
        logo_img = request.FILES.get('logo_img')
        pc_banner1 = request.FILES.get('pc_banner_1')
        mobile_banner1 = request.FILES.get('mobile_banner_1')

        try:
            shopconfig = ShopConfig.objects.last()
            if not shopconfig:
                shopconfig = ShopConfig()
        except:
            shopconfig = ShopConfig()

        print(shopconfig.banner_pc1)

        if logo_img is not None and shopconfig.logo_img is None:
            shopconfig.logo_img = logo_img
        elif logo_img is not None and shopconfig.logo_img is not None:
            os.remove(shopconfig.logo_img.path)
            shopconfig.logo_img = logo_img



        if pc_banner1 is not None and shopconfig.banner_pc1 == '':
            shopconfig.banner_pc1 = pc_banner1
        elif pc_banner1 is not None and shopconfig.banner_pc1 != '':
            os.remove(shopconfig.banner_pc1.path)
            shopconfig.banner_pc1 = pc_banner1

        if mobile_banner1 is not None and shopconfig.banner_mobile1 == '':
            shopconfig.banner_mobile1 = mobile_banner1
        elif mobile_banner1 is not None and shopconfig.banner_mobile1 != '':
            os.remove(shopconfig.banner_mobile1.path)
            shopconfig.banner_mobile1 = mobile_banner1

        shopconfig.save()

    return render(request, 'shopconfigapp/shop_config.html')




def test(request):
    return render(request, 'shopconfigapp/test.html', )





def shop_group(request):
    if request.method == 'POST':
        if request.POST.get('add_arate') == "addbtn":
            shopcate = ShopCategory()
            cate_list = ShopCategory.objects.last()
            if not cate_list:
                shopcate.ca_id = '10'
                shopcate.save()
            else:
                cate_first = cate_list.ca_id[0:1]
                intCate = int(cate_first)
                makeCate = intCate + 1
                shopcate.ca_id = f'{makeCate}0'
                shopcate.save()

        return HttpResponseRedirect('/cfg/shop_group')

    cate_list = ShopCategory.objects.all().order_by('ca_id')
    chk_html = 'shopconfigapp/shop_group.html'
    return render(request, chk_html, {'cate_list': cate_list})


def item_list(request):
    context = {}

    all_items = ShopItem.objects.all()

    category_list = []

    for i, item in enumerate(all_items):
        get_ca_list = []
        try:
            get_a_rate = ShopCategory.objects.get(ca_rate='A', ca_id=item.ca_id)
            get_ca_list.append(get_a_rate.ca_name)
        except:
            pass

        try:
            get_b_rate = ShopCategory.objects.get(ca_rate='B', ca_id=item.ca_id2)
            get_ca_list.append(get_b_rate.ca_name)
        except:
            pass

        try:
            get_c_rate = ShopCategory.objects.get(ca_rate='C', ca_id=item.ca_id3)
            get_ca_list.append(get_c_rate.ca_name)
        except:
            pass

        category_list.append(get_ca_list)

    # context['all_items'] = all_items
    # context['category_list'] = category_list

    all_item_list = zip(all_items, category_list)
    context['all_items'] = all_item_list

    return render(request, 'shopconfigapp/item_list.html', context)


def work_ajax(request):
    jsonObject = json.loads(request.body)

    if 'now_caid' in jsonObject:
        if len(jsonObject['now_caid']) == 2:
            make_cate_id(jsonObject['now_caid'], 'B', 2, 3)

        if len(jsonObject['now_caid']) == 4:
            make_cate_id(jsonObject['now_caid'], 'C', 4, 5)
    if 'update_caid' in jsonObject:
        choice_cate = ShopCategory.objects.get(ca_id=jsonObject['update_caid'])
        choice_cate.ca_name = jsonObject['get_name']
        choice_cate.save()

    if 'category_val' in jsonObject:
        if len(jsonObject['category_val']) == 2:
            get_category = ShopCategory.objects.filter(ca_rate='B', ca_id__startswith=jsonObject['category_val'])
            cate_dict = {'ca_id': [], 'ca_name': []}
            for cate in get_category:
                cate_dict['ca_id'].append(cate.ca_id)
                cate_dict['ca_name'].append(cate.ca_name)
        if len(jsonObject['category_val']) == 4:
            get_category = ShopCategory.objects.filter(ca_rate='C', ca_id__startswith=jsonObject['category_val'])
            cate_dict = {'ca_id': [], 'ca_name': []}
            for cate in get_category:
                cate_dict['ca_id'].append(cate.ca_id)
                cate_dict['ca_name'].append(cate.ca_name)
        jsonObject = cate_dict

    return JsonResponse(jsonObject)
    # return jsonObject


def make_cate_id(req, rate, start, end):
    shopcate = ShopCategory()
    cate_list = ShopCategory.objects.filter(ca_rate=f'{rate}', ca_id__startswith=req).last()
    if cate_list is None:
        shopcate.ca_id = f"{req}10"
        shopcate.ca_rate = f'{rate}'
        shopcate.save()
    else:
        cate_str_one = cate_list.ca_id[start:end]
        intCate = int(cate_str_one)
        makeCate = intCate + 1
        shopcate.ca_id = f"{req}{makeCate}0"
        shopcate.ca_rate = f'{rate}'
        shopcate.save()


def make_key():
    # 상품 아이디 (Key 값) 생성
    time = datetime.datetime.now().strftime("%m%d")
    result_key = f"1{time}"
    for i in range(5):
        temp_val = random.randrange(1, 10)
        result_key += str(temp_val)
    return result_key

# 가변 변수 연습 잘함
# for tong in tong_list:
#     globals()['it_{}_fprice'.format(tong)] = request.POST.get(f'it_{tong}_fprice')
#     globals()['it_{}_capa'.format(tong)] = request.POST.get(f'it_{tong}_capa')
#     globals()['it_{}_gongsi'.format(tong)] = request.POST.get(f'it_{tong}_gongsi')
#     globals()['it_{}_new_dc'.format(tong)] = request.POST.get(f'it_{tong}_new_dc')
#     globals()['it_{}_mnp_g_dc'.format(tong)] = request.POST.get(f'it_{tong}_mnp_g_dc')
#     globals()['it_{}_mnp_s_dc'.format(tong)] = request.POST.get(f'it_{tong}_mnp_s_dc')
#     globals()['it_{}_gib_g_dc'.format(tong)] = request.POST.get(f'it_{tong}_gib_g_dc')
#     globals()['it_{}_gib_s_dc'.format(tong)] = request.POST.get(f'it_{tong}_gib_s_dc')