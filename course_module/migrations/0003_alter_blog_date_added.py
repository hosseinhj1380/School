# Generated by Django 4.2 on 2023-04-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0002_blog_alter_course_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateField(auto_created=True, verbose_name='زمان انتشار'),
        ),
    ]
