# Generated by Django 3.0.4 on 2020-03-31 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='Joe', max_length=100)),
                ('lastName', models.CharField(default='Average', max_length=100)),
                ('skills', models.CharField(default='Housekeeper', max_length=20)),
                ('availableNow', models.BooleanField(default=True)),
            ],
        ),
    ]
