# Generated by Django 4.2.7 on 2023-11-27 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, validators=[main.utils.validate_phone_number], verbose_name='Номер телефона')),
                ('amount', models.PositiveBigIntegerField(verbose_name='Сумма')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания')),
            ],
            options={
                'verbose_name': 'Пополнение баланса',
                'verbose_name_plural': 'Пополнения баланса',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_phone', models.CharField(max_length=20, validators=[main.utils.validate_phone_number], verbose_name='Номер телефона отправителя')),
                ('recipient_phone', models.CharField(max_length=20, validators=[main.utils.validate_phone_number], verbose_name='Номер телефона получателя')),
                ('amount', models.PositiveBigIntegerField(verbose_name='Сумма перевода')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Картинка должна быть х на х', null=True, upload_to='profile_image/', verbose_name='Фотография профиля')),
                ('phone', models.CharField(help_text='Укажите действующий номер телефона', max_length=20, unique=True, validators=[main.utils.validate_phone_number], verbose_name='Телефон')),
                ('balance', models.PositiveBigIntegerField(default=0, help_text='Баланс', verbose_name='Баланс')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания')),
                ('user', models.OneToOneField(help_text='Связанный пользователь для данного профиля', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['-created_at'],
            },
        ),
    ]
