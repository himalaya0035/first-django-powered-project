# Generated by Django 3.0.8 on 2020-07-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc1', models.CharField(max_length=8)),
                ('desc2', models.CharField(blank=True, max_length=8, null=True)),
                ('desc3', models.CharField(blank=True, max_length=8, null=True)),
                ('price1', models.DecimalField(decimal_places=2, max_digits=7)),
                ('price2', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price3', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]