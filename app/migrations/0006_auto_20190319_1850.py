# Generated by Django 2.1.7 on 2019-03-19 18:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190319_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='phoneNum',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$')]),
        ),
    ]
