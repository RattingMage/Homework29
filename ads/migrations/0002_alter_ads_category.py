# Generated by Django 4.1.5 on 2023-01-15 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category'),
        ),
    ]