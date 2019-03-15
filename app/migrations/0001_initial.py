# Generated by Django 2.1.7 on 2019-03-15 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('author', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('postion', models.TextField()),
                ('benefits', models.TextField()),
                ('streetNum', models.IntegerField()),
                ('streetName', models.TextField()),
                ('townName', models.TextField()),
                ('state', models.TextField()),
                ('zipCode', models.IntegerField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.BlogPost'),
        ),
    ]
