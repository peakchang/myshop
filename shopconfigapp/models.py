from django.db import models
from django_quill.fields import QuillField


RATE_CHOICE = (('A', 'A분류'), ('B', 'B분류'), ('C', 'C분류'))

# Create your models here.
class ShopCategory(models.Model):
    ca_id = models.CharField(max_length=50)
    ca_rate = models.CharField(choices=RATE_CHOICE, max_length=20, null=True, default='A')
    ca_name = models.CharField(max_length=150)


class ShopConfig(models.Model):
    logo_img = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_pc1 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_mobile1 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_pc2 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_mobile2 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_pc3 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_mobile3 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_pc4 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_mobile4 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_pc5 = models.ImageField(upload_to='basic/', null=True, blank=True)
    banner_mobile5 = models.ImageField(upload_to='basic/', null=True, blank=True)


class ShopItem(models.Model):
    it_id = models.CharField(max_length=20, null=False)
    ca_id = models.CharField(max_length=20, null=True, default='')
    ca_id2 = models.CharField(max_length=20, null=True, default='')
    ca_id3 = models.CharField(max_length=20, null=True, default='')
    it_skin = models.CharField(max_length=20, null=True, default='')
    it_name = models.CharField(max_length=255, default='')
    it_sub_name = models.CharField(max_length=255, default='')
    it_depend_item = models.CharField(max_length=20, default='', null=True)
    it_main_item = models.BooleanField(default=False)
    it_co_type = models.CharField(max_length=20, default='', null=True)
    it_info = models.TextField(default='', null=True)
    it_model = models.CharField(max_length=255, default='', null=True)
    it_jisho_status = models.CharField(max_length=25, default='', null=True)
    it_type1 = models.BooleanField(default=False)
    it_type2 = models.BooleanField(default=False)
    it_type3 = models.BooleanField(default=False)
    it_type4 = models.BooleanField(default=False)
    it_type5 = models.BooleanField(default=False)
    it_seq = models.IntegerField(default=0, null=True)
    it_explain = models.TextField(default='', null=True)
    it_sub_explain = models.TextField(default='', null=True)
    it_cust_price = models.IntegerField(default=0, null=True)
    it_price = models.IntegerField(default=0, null=True)
    it_use = models.BooleanField(default=False)
    it_quantity = models.IntegerField(default=999)
    it_sc_type = models.CharField(max_length=20, default='', null=True)
    it_sc_price = models.IntegerField(default=0, null=True)
    it_buy_min_qty = models.IntegerField(default=0, null=True)
    it_buy_max_qty = models.IntegerField(default=10, null=True)
    it_hit = models.IntegerField(default=0, null=True)
    it_time = models.DateTimeField(auto_now_add=True)
    it_update_time = models.DateTimeField(auto_now_add=True)
    it_option = models.TextField(default='', null=True)
    it_add_product = models.TextField(default='', null=True)
    it_use_count = models.IntegerField(default=0, null=True)
    it_use_average = models.FloatField(default=0.0, null=True)
    it_naver_category = models.CharField(max_length=20, default='', null=True)
    it_color = models.CharField(max_length=255, default='', null=True)
    it_color_code = models.CharField(max_length=255, default='', null=True)
    it_img1 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img2 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img3 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img4 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img5 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img6 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img7 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img8 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_img9 = models.ImageField(upload_to='item_img/', null=True, blank=True)
    it_sk_fprice = models.CharField(max_length=100, default='', null=True)
    it_sk_capa = models.CharField(max_length=100, default='', null=True)
    it_sk_gongsi = models.CharField(max_length=100, default='', null=True)
    it_sk_new_dc = models.CharField(max_length=100, default='', null=True)
    it_sk_mnp_g_dc = models.CharField(max_length=100, default='', null=True)
    it_sk_mnp_s_dc = models.CharField(max_length=100, default='', null=True)
    it_sk_gib_g_dc = models.CharField(max_length=100, default='', null=True)
    it_sk_gib_s_dc = models.CharField(max_length=100, default='', null=True)
    it_kt_fprice = models.CharField(max_length=100, default='', null=True)
    it_kt_capa = models.CharField(max_length=100, default='', null=True)
    it_kt_gongsi = models.CharField(max_length=100, default='', null=True)
    it_kt_new_dc = models.CharField(max_length=100, default='', null=True)
    it_kt_mnp_g_dc = models.CharField(max_length=100, default='', null=True)
    it_kt_mnp_s_dc = models.CharField(max_length=100, default='', null=True)
    it_kt_gib_g_dc = models.CharField(max_length=100, default='', null=True)
    it_kt_gib_s_dc = models.CharField(max_length=100, default='', null=True)
    it_lg_fprice = models.CharField(max_length=100, default='', null=True)
    it_lg_capa = models.CharField(max_length=100, default='', null=True)
    it_lg_gongsi = models.CharField(max_length=100, default='', null=True)
    it_lg_new_dc = models.CharField(max_length=100, default='', null=True)
    it_lg_mnp_g_dc = models.CharField(max_length=100, default='', null=True)
    it_lg_mnp_s_dc = models.CharField(max_length=100, default='', null=True)
    it_lg_gib_g_dc = models.CharField(max_length=100, default='', null=True)
    it_lg_gib_s_dc = models.CharField(max_length=100, default='', null=True)


class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title
