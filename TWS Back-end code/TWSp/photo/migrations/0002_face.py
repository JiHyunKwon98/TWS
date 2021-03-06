# Generated by Django 3.0.8 on 2020-07-30 12:21

from django.db import migrations, models
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=32, verbose_name='face 이름')),
                ('fimage', photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m', verbose_name='face 이미지')),
            ],
            options={
                'db_table': 'Face',
            },
        ),
    ]
