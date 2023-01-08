# Generated by Django 4.0.6 on 2022-07-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garage_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('hourly_cost', models.IntegerField(default=750)),
            ],
        ),
    ]