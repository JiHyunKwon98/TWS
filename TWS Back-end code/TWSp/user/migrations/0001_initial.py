# Generated by Django 3.0.8 on 2020-07-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=32, verbose_name='사용자 이름')),
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='사용자 아이디')),
                ('pw', models.CharField(max_length=64, verbose_name='사용자 비밀번호')),
                ('pwc', models.CharField(max_length=64, verbose_name='비밀번호 확인')),
                ('company', models.CharField(max_length=128, verbose_name='업체명')),
                ('address', models.CharField(max_length=256, verbose_name='업체주소')),
                ('call', models.CharField(blank=True, max_length=128, verbose_name='업체번호')),
                ('email', models.CharField(blank=True, max_length=128, verbose_name='사용자 이메일')),
            ],
        ),
    ]