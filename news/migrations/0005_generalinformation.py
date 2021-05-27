# Generated by Django 3.2.3 on 2021-05-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Общая информация',
                'verbose_name_plural': 'Общей информации',
            },
        ),
    ]
