# Generated by Django 3.1.5 on 2021-01-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]