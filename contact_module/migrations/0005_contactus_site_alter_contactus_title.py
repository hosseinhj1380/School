# Generated by Django 4.1.2 on 2023-05-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0004_alter_contactus_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='site',
            field=models.CharField(default='', max_length=300, verbose_name='وبسایت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=300, verbose_name='عنوان'),
        ),
    ]
