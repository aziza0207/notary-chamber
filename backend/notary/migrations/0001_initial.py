# Generated by Django 4.2.5 on 2023-10-30 12:10

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
                ('region', models.CharField(choices=[('Джалал-Абад', 'Djalal Abad'), ('Бишкек', 'Bishkek'), ('Каnt', 'Kant')], verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Нотариус',
                'verbose_name_plural': 'Нотариусы',
                'ordering': ['id'],
            },
        ),
    ]
