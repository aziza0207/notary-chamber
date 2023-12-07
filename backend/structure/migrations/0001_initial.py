# Generated by Django 4.2.5 on 2023-12-07 10:22

from django.db import migrations, models
import django.db.models.deletion
import structure.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=structure.models.department_images, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Комиссия',
                'verbose_name_plural': 'Комиссии',
            },
        ),
        migrations.CreateModel(
            name='GeneralAssembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=structure.models.department_images, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Общее собрание',
                'verbose_name_plural': 'Общие собрания',
            },
        ),
        migrations.CreateModel(
            name='NotaryCouncil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=structure.models.department_images, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NotaryCouncilWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('full_name_ru', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('full_name_ky', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('full_name_en', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, null=True, upload_to=structure.models.department_worker_files, verbose_name='Изображение')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='structure.notarycouncil', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralAssemblyWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('full_name_ru', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('full_name_ky', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('full_name_en', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, null=True, upload_to=structure.models.department_worker_files, verbose_name='Изображение')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='structure.generalassembly', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComissionWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('full_name_ru', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('full_name_ky', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('full_name_en', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, null=True, upload_to=structure.models.department_worker_files, verbose_name='Изображение')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='structure.comission', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
