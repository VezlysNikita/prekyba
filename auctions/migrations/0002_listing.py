# Generated by Django 3.2.9 on 2022-02-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
