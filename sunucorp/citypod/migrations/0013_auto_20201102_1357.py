# Generated by Django 3.1.1 on 2020-11-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citypod', '0012_auto_20201026_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubName', models.CharField(max_length=50)),
                ('pubDescription', models.TextField()),
                ('pubFile', models.FileField(blank=True, null=True, upload_to='filePub')),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='pageFile',
            field=models.FileField(blank=True, null=True, upload_to='filePage'),
        ),
    ]
