# Generated by Django 3.2.3 on 2021-05-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210520_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='blog.Category'),
        ),
    ]
