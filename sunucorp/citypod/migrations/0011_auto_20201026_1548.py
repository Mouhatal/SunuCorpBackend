# Generated by Django 3.1.1 on 2020-10-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citypod', '0010_auto_20201026_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subCategoryImg',
            field=models.ImageField(blank=True, null=True, upload_to='./image/subcategorie'),
        ),
    ]
