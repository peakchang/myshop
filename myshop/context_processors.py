# context_processors.py
import os
from pathlib import Path

import media
from django.utils import timezone


def message_processor(request):
    # chk_root = Path(__file__).resolve().parent.parent
    sample_media_dir = f'http:\\\\{request.get_host()}\\media\\sample\\'

    print(sample_media_dir)
    try:
        base_time = timezone.now().strftime ("%m%d%M%S")
        print(base_time)


    except:
        pass
    return {'base_time': base_time, 'sample_media_dir': sample_media_dir}