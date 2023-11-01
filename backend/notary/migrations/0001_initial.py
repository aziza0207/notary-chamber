# Generated by Django 4.2.5 on 2023-11-01 09:39

from django.db import migrations, models
import notary.models.notary_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=notary.models.notary_model.notary_photos, verbose_name='Фото')),
                ('city', models.CharField(choices=[('Джалал-Абад', 'Djalal Abad'), ('Бишкек', 'Bishkek'), ('Каnt', 'Kant')], verbose_name='Город')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('region', models.CharField(choices=[('Джалал-Абад', 'Djalal Abad'), ('Бишкек', 'Bishkek'), ('Каnt', 'Kant')], verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Нотариус',
                'verbose_name_plural': 'Нотариусы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Получатель рассылки',
                'verbose_name_plural': 'Получатели рассылки',
                'ordering': ['id'],
            },
        ),
    ]
