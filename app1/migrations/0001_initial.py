# Generated by Django 4.2 on 2023-04-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=250)),
                ('category', models.CharField(max_length=20)),
                ('provider', models.CharField(max_length=200)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
