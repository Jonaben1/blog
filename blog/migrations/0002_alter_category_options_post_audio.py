# Generated by Django 4.2.1 on 2023-08-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio/'),
        ),
    ]
