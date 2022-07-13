# context_processors.py
import os
from pathlib import Path

import media
from django.utils import timezone

from shopconfigapp.models import ShopConfig


def message_processor(request):
    # chk_root = Path(__file__).resolve().parent.parent
    try:
        shop_base = ShopConfig.objects.last()
    except:
        shop_base = {}
    sample_media_dir = f'http:\\\\{request.get_host()}\\media\\sample\\'
    try:
        base_time = timezone.now().strftime ("%m%d%M%S")
    except:
        pass

    print(shop_base)


    return {'base_time': base_time, 'sample_media_dir': sample_media_dir, 'shop_base': shop_base}