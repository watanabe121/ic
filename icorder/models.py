from django.db import models
from django.urls import reverse
from django.utils import timezone
from .choice import MEDIA_STYLE, PLATE_LAMI_STYLE, POSTER_LAMI_STYLE, FUCHI_STYLE, SQUARE_STYLE, \
    PRINT_STYLE, WHITE_INK_STYLE, SHEET_CUT, PANEL_STYLE, DATA_SEND, SHIPPING_STYLE, VARIABLE_STYLE, CUSTOMER_INDUSTRY, \
    OUTPUT_LOCATION, PAPER_STYLE, PACKING_STYLE, FUCHI


class Customer(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name='顧客名')
    sales_staff = models.CharField(max_length=100, verbose_name='営業担当')
    order_number = models.IntegerField(verbose_name='受注No.')
    shipping_day = models.DateField(verbose_name='出荷日')
    shipping_time = models.TimeField(verbose_name='仕上時間', blank=True)
    packing_type = models.CharField(max_length=20, verbose_name='梱包形態', choices=PACKING_STYLE, default='通常')
    shipping_style = models.CharField(max_length=50, verbose_name='出荷方法', choices=SHIPPING_STYLE)
    data = models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ', choices=DATA_SEND)
    data_location = models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ場所')
    data_details = models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ詳細')
    output_style = models.CharField(max_length=100, verbose_name='出力', choices=OUTPUT_LOCATION)

    def __str__(self):
        return self.customer_name + ' ' + '|' + ' ' + str(self.order_number)


class PrintLami(models.Model):
    media_style = models.CharField(max_length=30, verbose_name='ﾒﾃﾞｨｱ', choices=MEDIA_STYLE, blank=True)
    white_ink_style = models.CharField(max_length=10, verbose_name='白ｲﾝｸ', choices=WHITE_INK_STYLE, blank=True)
    sheet_cut = models.CharField(max_length=10, verbose_name='紙ｶｯﾄ', choices=SHEET_CUT, blank=True)
    lami_style = models.CharField(max_length=30, verbose_name='ﾗﾐ', choices=POSTER_LAMI_STYLE, blank=True)
    fuchi = models.CharField(max_length=10, verbose_name='ﾌﾁ', choices=FUCHI)
    fuchi_size = models.IntegerField(verbose_name='ﾌﾁｻｲｽﾞ')
    square_style = models.CharField(max_length=10, verbose_name='角丸', choices=SQUARE_STYLE)
    panel_style = models.CharField(max_length=20, verbose_name='ﾊﾟﾈﾙ', choices=PANEL_STYLE)
    high_size = models.IntegerField(verbose_name='縦')
    wide_size = models.IntegerField(verbose_name='横')
    quintity = models.IntegerField(verbose_name='枚数')
    print_contents = models.CharField(max_length=255, verbose_name='印刷物の内容', blank=True)
    second_processing = models.CharField(max_length=255, verbose_name='その他二次加工', blank=True)
    created_date = models.DateTimeField(verbose_name='入力日', default=timezone.now, null=True)
    customer_name = models.ForeignKey(Customer, verbose_name='顧客名', blank=True, null=True, on_delete=models.SET_NULL)


class PlateCustomer(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name='顧客名')
    sales_staff = models.CharField(max_length=100, verbose_name='営業担当')
    order_number = models.IntegerField(verbose_name='受注No.')
    customer_industry = models.CharField(max_length=30, verbose_name='業種', choices=CUSTOMER_INDUSTRY)
    shipping_day = models.DateField(verbose_name='出荷日')
    shipping_time = models.TimeField(verbose_name='仕上時間', blank=True)
    packing_type = models.CharField(max_length=20, verbose_name='梱包形態', choices=PACKING_STYLE, default='通常')
    shipping_style = models.CharField(max_length=50, verbose_name='出荷方法', choices=SHIPPING_STYLE)
    data = models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ', choices=DATA_SEND)
    data_location = models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ場所')
    data_details = models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ詳細')
    output_style = models.CharField(max_length=100, verbose_name='出力', choices=OUTPUT_LOCATION)

    def __str__(self):
        return self.customer_name + ' ' + '|' + ' ' + str(self.order_number)


class Plate(models.Model):
    output = models.CharField(max_length=20, verbose_name='片・両', blank=True, choices=PRINT_STYLE, default='両面')
    paper_style = models.CharField(max_length=20, verbose_name='紙種', blank=True, choices=PAPER_STYLE)
    variable = models.CharField(max_length=20, verbose_name='ﾊﾞﾘｱﾌﾞﾙ', blank=True, choices=VARIABLE_STYLE, default='無')
    high_size = models.IntegerField(verbose_name='縦')
    wide_size = models.IntegerField(verbose_name='横')
    quintity = models.IntegerField(verbose_name='枚数')
    plate_lami_style = models.CharField(max_length=20, verbose_name='ﾗﾐ', choices=PLATE_LAMI_STYLE, default='250M')
    fuchi_style = models.CharField(max_length=20, verbose_name='ﾌﾁ種', choices=FUCHI_STYLE, default='差込口')
    fuchi = models.IntegerField(verbose_name='ﾌﾁ')
    square_style = models.CharField(max_length=20, verbose_name='角丸', choices=SQUARE_STYLE, default='有')
    print_contents = models.CharField(max_length=255, verbose_name='印刷物の内容', blank=True)
    second_processing = models.CharField(max_length=255, verbose_name='その他二次加工', blank=True)
    paper_mold = models.IntegerField(verbose_name='型No.紙')
    lami_mold = models.IntegerField(verbose_name='型No.ﾗﾐ')
    created_date = models.DateTimeField(verbose_name='入力日', default=timezone.now, null=True)
    customer_name = models.ForeignKey(PlateCustomer, verbose_name='顧客名', blank=True, null=True,
                                      on_delete=models.SET_NULL)
