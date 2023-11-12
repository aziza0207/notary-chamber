# Generated by Django 4.2.5 on 2023-11-12 10:13

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models

import content.models.documents_model
import content.models.gallery_models
import content.models.news_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('is_visible', models.BooleanField(default=False, verbose_name='Виден на сайте')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('file', models.FileField(upload_to=content.models.documents_model.document_files, verbose_name='Файл')),
                ('file_ru', models.FileField(null=True, upload_to=content.models.documents_model.document_files, verbose_name='Файл')),
                ('file_ky', models.FileField(null=True, upload_to=content.models.documents_model.document_files, verbose_name='Файл')),
                ('file_en', models.FileField(null=True, upload_to=content.models.documents_model.document_files, verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Все документы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('question_ru', models.CharField(max_length=255, null=True, verbose_name='Вопрос')),
                ('question_ky', models.CharField(max_length=255, null=True, verbose_name='Вопрос')),
                ('question_en', models.CharField(max_length=255, null=True, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('answer_ru', models.TextField(null=True, verbose_name='Ответ')),
                ('answer_ky', models.TextField(null=True, verbose_name='Ответ')),
                ('answer_en', models.TextField(null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Частые вопросы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('link', models.URLField(max_length=300, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Полезная ссылка',
                'verbose_name_plural': 'Полезные ссылки',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=content.models.news_model.news_main_image, verbose_name='Основное изображение')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Слаг')),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('video', models.URLField(blank=True, null=True, verbose_name='Линк на ютуб')),
                ('date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='Закрепленные')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='Рекомендованные')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date', 'is_pinned'],
            },
        ),
        migrations.CreateModel(
            name='PhotoSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, help_text='Уникальное поле. Автоматически генерируется\n                         из названия. Используется в качестве адреса страницы', populate_from='title', unique=True, verbose_name='Слаг')),
                ('image', models.ImageField(upload_to=content.models.gallery_models.gallery_files, verbose_name='Обложка')),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Фотосет',
                'verbose_name_plural': 'Фотосеты',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('link', models.URLField(max_length=300, verbose_name='Ссылка')),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=content.models.gallery_models.gallery_files, verbose_name='Изображение')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('photoset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='content.photoset', verbose_name='Фотосет')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=content.models.news_model.news_images, verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='content.news', verbose_name='Новости')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
