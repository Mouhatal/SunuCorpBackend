# Generated by Django 3.1.1 on 2020-09-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citypod', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subImgCategory',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
