# Generated by Django 4.0.6 on 2022-07-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca_id', models.CharField(max_length=50)),
                ('ca_rate', models.CharField(choices=[('A', 'A분류'), ('B', 'B분류'), ('C', 'C분류')], default='A', max_length=20, null=True)),
                ('ca_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ShopConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_pc1', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_mobile1', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_pc2', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_mobile2', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_pc3', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_mobile3', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_pc4', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_mobile4', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_pc5', models.ImageField(blank=True, null=True, upload_to='basic/')),
                ('banner_mobile5', models.ImageField(blank=True, null=True, upload_to='basic/')),
            ],
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('it_id', models.CharField(max_length=20)),
                ('ca_id', models.CharField(default='', max_length=20, null=True)),
                ('ca_id2', models.CharField(default='', max_length=20, null=True)),
                ('ca_id3', models.CharField(default='', max_length=20, null=True)),
                ('it_skin', models.CharField(default='', max_length=20, null=True)),
                ('it_name', models.CharField(default='', max_length=255)),
                ('it_sub_name', models.CharField(default='', max_length=255)),
                ('it_depend_item', models.CharField(default='', max_length=20, null=True)),
                ('it_main_item', models.BooleanField(default=False)),
                ('it_co_type', models.CharField(default='', max_length=20, null=True)),
                ('it_info', models.TextField(default='', null=True)),
                ('it_model', models.CharField(default='', max_length=255, null=True)),
                ('it_jisho_status', models.CharField(default='', max_length=25, null=True)),
                ('it_type1', models.BooleanField(default=False)),
                ('it_type2', models.BooleanField(default=False)),
                ('it_type3', models.BooleanField(default=False)),
                ('it_type4', models.BooleanField(default=False)),
                ('it_type5', models.BooleanField(default=False)),
                ('it_seq', models.IntegerField(default=0, null=True)),
                ('it_explain', models.TextField(default='', null=True)),
                ('it_sub_explain', models.TextField(default='', null=True)),
                ('it_cust_price', models.IntegerField(default=0, null=True)),
                ('it_price', models.IntegerField(default=0, null=True)),
                ('it_use', models.BooleanField(default=False)),
                ('it_quantity', models.IntegerField(default=999)),
                ('it_sc_type', models.CharField(default='', max_length=20, null=True)),
                ('it_sc_price', models.IntegerField(default=0, null=True)),
                ('it_buy_min_qty', models.IntegerField(default=0, null=True)),
                ('it_buy_max_qty', models.IntegerField(default=10, null=True)),
                ('it_hit', models.IntegerField(default=0, null=True)),
                ('it_time', models.DateTimeField(auto_now_add=True)),
                ('it_update_time', models.DateTimeField(auto_now_add=True)),
                ('it_option', models.TextField(default='', null=True)),
                ('it_add_product', models.TextField(default='', null=True)),
                ('it_use_count', models.IntegerField(default=0, null=True)),
                ('it_use_average', models.FloatField(default=0.0, null=True)),
                ('it_naver_category', models.CharField(default='', max_length=20, null=True)),
                ('it_color', models.CharField(default='', max_length=255, null=True)),
                ('it_color_code', models.CharField(default='', max_length=255, null=True)),
                ('it_img1', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img2', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img3', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img4', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img5', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img6', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img7', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img8', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_img9', models.ImageField(blank=True, null=True, upload_to='item_img/')),
                ('it_sk_fprice', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_capa', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_gongsi', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_new_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_mnp_g_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_mnp_s_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_gib_g_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_sk_gib_s_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_fprice', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_capa', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_gongsi', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_new_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_mnp_g_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_mnp_s_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_gib_g_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_kt_gib_s_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_fprice', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_capa', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_gongsi', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_new_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_mnp_g_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_mnp_s_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_gib_g_dc', models.CharField(default='', max_length=100, null=True)),
                ('it_lg_gib_s_dc', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
    ]
