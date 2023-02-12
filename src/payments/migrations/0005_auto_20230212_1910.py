# Generated by Django 3.2.9 on 2023-02-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20230212_1900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'default_related_name': 'Orders', 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Orders', to='payments.discount', verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Orders', to='payments.tax', verbose_name='Tax'),
        ),
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(choices=[('eur', 'EURO'), ('usd', 'USD')], default='eur', max_length=12, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='Orders', to='payments.Item', verbose_name='Item list'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='percent',
            field=models.FloatField(default=0, verbose_name='Percent'),
        ),
    ]