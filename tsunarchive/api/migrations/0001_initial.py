# Generated by Django 4.1.7 on 2023-02-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('gender', models.TextField(blank=True)),
                ('affiliation', models.TextField(blank=True)),
                ('hair_style', models.TextField(blank=True)),
                ('hair_color', models.TextField(blank=True)),
                ('Ttype', models.TextField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='characters')),
            ],
        ),
    ]
