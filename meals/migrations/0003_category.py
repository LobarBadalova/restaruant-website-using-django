# Generated by Django 3.1.1 on 2020-09-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20200908_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=200)),
            ],
        ),
    ]