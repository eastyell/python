# Generated by Django 2.2.4 on 2019-08-17 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('pub_date', models.DateField(verbose_name='发布时间')),
                ('author', models.CharField(default=None, max_length=64, verbose_name='作者')),
            ],
        ),
    ]
