# Generated by Django 3.1.1 on 2020-10-01 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citypod', '0004_auto_20201001_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='citypod.category'),
        ),
    ]
