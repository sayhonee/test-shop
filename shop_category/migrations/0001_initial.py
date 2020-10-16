# Generated by Django 3.1.2 on 2020-10-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('name', models.CharField(max_length=150, verbose_name='عنوان در url')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
    ]
