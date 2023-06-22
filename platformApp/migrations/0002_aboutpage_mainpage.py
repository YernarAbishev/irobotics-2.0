# Generated by Django 3.1 on 2022-11-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platformApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание страницы о проекте')),
            ],
            options={
                'verbose_name': 'Cтраница О проекте',
                'verbose_name_plural': 'Cтраница О проекте',
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание главной страницы')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
    ]
