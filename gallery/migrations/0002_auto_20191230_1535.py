# Generated by Django 2.0.2 on 2019-12-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='这里写描述', max_length=50),
        ),
    ]
