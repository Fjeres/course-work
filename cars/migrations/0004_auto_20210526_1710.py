# Generated by Django 3.2.3 on 2021-05-26 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210524_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='carModel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.carmodel', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='title',
            field=models.CharField(default='Lada', max_length=4, verbose_name='Марка'),
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.carmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Аксессуар',
                'verbose_name_plural': 'Аксессуары',
            },
        ),
    ]
