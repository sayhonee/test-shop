# Generated by Django 3.1.2 on 2020-10-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name='موضوع')),
                ('text', models.CharField(max_length=300, verbose_name='متن پیام')),
                ('is_read', models.BooleanField(verbose_name='خوانده شده/ نشده')),
            ],
            options={
                'verbose_name': 'تماس باما',
                'verbose_name_plural': 'تماس های کاربران',
            },
        ),
    ]
