# Generated by Django 5.2.2 on 2025-06-07 14:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerdetail',
            old_name='url',
            new_name='title',
        ),
        migrations.AddField(
            model_name='offerdetail',
            name='delivery_time_in_days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerdetail',
            name='features',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerdetail',
            name='offer_type',
            field=models.CharField(default='basic', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerdetail',
            name='revisions',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='offers/'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='min_delivery_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
