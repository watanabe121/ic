# Generated by Django 3.2 on 2021-04-12 01:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, verbose_name='顧客名')),
                ('sales_staff', models.CharField(max_length=100, verbose_name='営業担当')),
                ('order_number', models.IntegerField(verbose_name='受注No.')),
                ('shipping_day', models.DateField(verbose_name='出荷日')),
                ('shipping_time', models.TimeField(blank=True, verbose_name='仕上時間')),
                ('packing_type', models.CharField(choices=[('通常', '通常'), ('仕分有', '仕分有'), ('複数送付有', '複数送付有'), ('予備同送', '予備同送'), ('予備営業へ', '予備営業へ')], default='通常', max_length=20, verbose_name='梱包形態')),
                ('shipping_style', models.CharField(choices=[('引取', '引取'), ('納品', '納品'), ('施工', '施工'), ('発送', '発送'), ('支店入れ', '支店入れ')], max_length=50, verbose_name='出荷方法')),
                ('data', models.CharField(choices=[('自社', '自社'), ('外注', '外注'), ('支給', '支給')], max_length=100, verbose_name='ﾃﾞｰﾀ')),
                ('data_location', models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ場所')),
                ('data_details', models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ詳細')),
                ('output_style', models.CharField(choices=[('自社', '自社'), ('外注', '外注'), ('支給', '支給')], max_length=100, verbose_name='出力')),
            ],
        ),
        migrations.CreateModel(
            name='PlateCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, verbose_name='顧客名')),
                ('sales_staff', models.CharField(max_length=100, verbose_name='営業担当')),
                ('order_number', models.IntegerField(verbose_name='受注No.')),
                ('customer_industry', models.CharField(choices=[('一般', '一般'), ('P', 'P')], max_length=30, verbose_name='業種')),
                ('shipping_day', models.DateField(verbose_name='出荷日')),
                ('shipping_time', models.TimeField(blank=True, verbose_name='仕上時間')),
                ('packing_type', models.CharField(choices=[('通常', '通常'), ('仕分有', '仕分有'), ('複数送付有', '複数送付有'), ('予備同送', '予備同送'), ('予備営業へ', '予備営業へ')], default='通常', max_length=20, verbose_name='梱包形態')),
                ('shipping_style', models.CharField(choices=[('引取', '引取'), ('納品', '納品'), ('施工', '施工'), ('発送', '発送'), ('支店入れ', '支店入れ')], max_length=50, verbose_name='出荷方法')),
                ('data', models.CharField(choices=[('自社', '自社'), ('外注', '外注'), ('支給', '支給')], max_length=100, verbose_name='ﾃﾞｰﾀ')),
                ('data_location', models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ場所')),
                ('data_details', models.CharField(max_length=100, verbose_name='ﾃﾞｰﾀ詳細')),
                ('output_style', models.CharField(choices=[('自社', '自社'), ('外注', '外注'), ('支給', '支給')], max_length=100, verbose_name='出力')),
            ],
        ),
        migrations.CreateModel(
            name='PrintLami',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_style', models.CharField(blank=True, choices=[('無し', '無し'), ('合成紙糊無し', '合成紙糊無し'), ('厚手コート', '厚手コート'), ('フォト用紙 EXCEL グロス', 'フォト用紙 EXCEL グロス'), ('フォト用紙 EXCEL マット', 'フォト用紙 EXCEL マット'), ('PPバナー', 'PPバナー'), ('防炎クロス', '防炎クロス'), ('合成紙グレー糊', '合成紙グレー糊'), ('合成紙クリア糊', '合成紙クリア糊'), ('合成紙 再剥離', '合成紙 再剥離'), ('MP合成紙', 'MP合成紙'), ('ボードメディア', 'ボードメディア'), ('水性PVCグレー糊', '水性PVCグレー糊'), ('PVCクリア糊', 'PVCクリア糊'), ('PETバナー', 'PETバナー'), ('イージーカットクロス', 'イージーカットクロス'), ('水性ポンジ', '水性ポンジ'), ('水性バックライト', '水性バックライト'), ('PETバナーブロックアウト', 'PETバナーブロックアウト'), ('水性PPグロスバナー', '水性PPグロスバナー'), ('PETバナーホワイト', 'PETバナーホワイト'), ('クリアフィルム 粘着', 'クリアフィルム 粘着'), ('エアスルーメディア', 'エアスルーメディア'), ('ハガセルホワイトPP', 'ハガセルホワイトPP'), ('水性PVCマトリクス', '水性PVCマトリクス'), ('水性ターポリン', '水性ターポリン'), ('ポップアップバナー', 'ポップアップバナー'), ('粘着クロス', '粘着クロス'), ('シースルークロス', 'シースルークロス'), ('吸着合成紙', '吸着合成紙'), ('3Dメディア 大玉', '3Dメディア 大玉'), ('3Dメディア 小玉', '3Dメディア 小玉'), ('溶剤PVCグレー糊', '溶剤PVCグレー糊'), ('溶剤フォト用紙 グロス', '溶剤フォト用紙 グロス'), ('溶剤フォト用紙 マット', '溶剤フォト用紙 マット'), ('溶剤ターポリンEXCEL', '溶剤ターポリンEXCEL'), ('溶剤PVCマトリクス', '溶剤PVCマトリクス'), ('溶剤PPバナー', '溶剤PPバナー'), ('溶剤PPグロスバナー', '溶剤PPグロスバナー'), ('溶剤PETバナー グロス', '溶剤PETバナー グロス'), ('溶剤PETバナー マット', '溶剤PETバナー マット'), ('溶剤ライトバナー', '溶剤ライトバナー'), ('溶剤バックライト', '溶剤バックライト'), ('溶剤クリアPET糊なし', '溶剤クリアPET糊なし'), ('溶剤クリアPET強粘着', '溶剤クリアPET強粘着'), ('溶剤クリア塩ビ強粘着', '溶剤クリア塩ビ強粘着'), ('溶剤ミラーゴールド', '溶剤ミラーゴールド'), ('溶剤ミラーシルバー', '溶剤ミラーシルバー'), ('溶剤ハガセルクリアPET', '溶剤ハガセルクリアPET'), ('溶剤３Dメディア 大玉', '溶剤３Dメディア 大玉'), ('溶剤３Dメディア 小玉', '溶剤３Dメディア 小玉'), ('溶剤スムースシルバー(糊付)', '溶剤スムースシルバー(糊付)'), ('溶剤スムースゴールド(糊付)', '溶剤スムースゴールド(糊付)'), ('溶剤ホログラム(スパークル)', '溶剤ホログラム(スパークル)'), ('溶剤屋外フロアアルミシート', '溶剤屋外フロアアルミシート'), ('溶剤屋外壁面アルミシート', '溶剤屋外壁面アルミシート')], max_length=30, verbose_name='ﾒﾃﾞｨｱ')),
                ('white_ink_style', models.CharField(blank=True, choices=[('有', '有'), ('無', '無')], max_length=10, verbose_name='白ｲﾝｸ')),
                ('sheet_cut', models.CharField(blank=True, choices=[('有', '有'), ('無', '無')], max_length=10, verbose_name='紙ｶｯﾄ')),
                ('lami_style', models.CharField(blank=True, choices=[('無し', '無し'), ('32mic', '32mic'), ('100mic', '100mic'), ('150mic', '150mic'), ('200mic', '200mic'), ('250mic', '250mic'), ('300mic', '300mic'), ('350mic', '350mic'), ('塩ビグロス', '塩ビグロス'), ('塩ビマット', '塩ビマット'), ('OPPグロス', 'OPPグロス'), ('OPPマット', 'OPPマット'), ('フロア床用エンボス', 'フロア床用エンボス'), ('キャンバス', 'キャンバス'), ('ハイグロスPET50', 'ハイグロスPET50'), ('スーパーグロス250PET', 'スーパーグロス250PET'), ('スーパー光沢フロア', 'スーパー光沢フロア'), ('ゴム用フロアマット', 'ゴム用フロアマット'), ('スラッシュラミ', 'スラッシュラミ'), ('ホログラム', 'ホログラム'), ('ウィンドウラミEXCEL', 'ウィンドウラミEXCEL'), ('ペイントラミ', 'ペイントラミ'), ('レインボーフィルム', 'レインボーフィルム')], max_length=30, verbose_name='ﾗﾐ')),
                ('fuchi', models.CharField(choices=[('有', '有'), ('無', '無'), ('ｵｰﾊﾞｰﾗﾐ', 'ｵｰﾊﾞｰﾗﾐ')], max_length=10, verbose_name='ﾌﾁ')),
                ('fuchi_size', models.IntegerField(verbose_name='ﾌﾁｻｲｽﾞ')),
                ('square_style', models.CharField(choices=[('有', '有'), ('無', '無')], max_length=10, verbose_name='角丸')),
                ('panel_style', models.CharField(choices=[('無し', '無し'), ('白片面', '白片面'), ('黒片面', '黒片面'), ('白両面', '白両面'), ('黒両面', '黒両面'), ('外注', '外注')], max_length=20, verbose_name='ﾊﾟﾈﾙ')),
                ('high_size', models.IntegerField(verbose_name='縦')),
                ('wide_size', models.IntegerField(verbose_name='横')),
                ('quintity', models.IntegerField(verbose_name='枚数')),
                ('print_contents', models.CharField(blank=True, max_length=255, verbose_name='印刷物の内容')),
                ('second_processing', models.CharField(blank=True, max_length=255, verbose_name='その他二次加工')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='入力日')),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='icorder.customer', verbose_name='顧客名')),
            ],
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.CharField(blank=True, choices=[('片面', '片面'), ('両面', '両面')], default='両面', max_length=20, verbose_name='片・両')),
                ('paper_style', models.CharField(blank=True, choices=[('135k 317x450', '135k 317x450'), ('220k 317X450', '220k 317X450'), ('135k 330x1090', '135k 330x1090'), ('220k 330x1260', '220k 330x1260')], max_length=20, verbose_name='紙種')),
                ('variable', models.CharField(blank=True, choices=[('有', '有'), ('無', '無')], default='無', max_length=20, verbose_name='ﾊﾞﾘｱﾌﾞﾙ')),
                ('high_size', models.IntegerField(verbose_name='縦')),
                ('wide_size', models.IntegerField(verbose_name='横')),
                ('quintity', models.IntegerField(verbose_name='枚数')),
                ('plate_lami_style', models.CharField(choices=[('無し', '無し'), ('32mic', '32mic'), ('100mic', '100mic'), ('150mic', '150mic'), ('200mic', '200mic'), ('250mic', '250mic'), ('300mic', '300mic'), ('350mic', '350mic')], default='250M', max_length=20, verbose_name='ﾗﾐ')),
                ('fuchi_style', models.CharField(choices=[('全無', '全無'), ('差込口', '差込口'), ('全有', '全有')], default='差込口', max_length=20, verbose_name='ﾌﾁ種')),
                ('fuchi', models.IntegerField(verbose_name='ﾌﾁ')),
                ('square_style', models.CharField(choices=[('有', '有'), ('無', '無')], default='有', max_length=20, verbose_name='角丸')),
                ('print_contents', models.CharField(blank=True, max_length=255, verbose_name='印刷物の内容')),
                ('second_processing', models.CharField(blank=True, max_length=255, verbose_name='その他二次加工')),
                ('paper_mold', models.IntegerField(verbose_name='型No.紙')),
                ('lami_mold', models.IntegerField(verbose_name='型No.ﾗﾐ')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='入力日')),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='icorder.platecustomer', verbose_name='顧客名')),
            ],
        ),
    ]
