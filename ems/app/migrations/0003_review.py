# Generated by Django 4.2.7 on 2023-11-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_slidemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='review/')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]