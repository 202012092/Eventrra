# Generated by Django 3.2.9 on 2021-11-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211113_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
