# Generated by Django 3.1.6 on 2021-02-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('address2', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=15)),
                ('zip', models.CharField(max_length=10)),
            ],
        ),
    ]
