# Generated by Django 4.1.3 on 2022-12-06 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opros', '0003_userinput_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user_input',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='opros.userinput', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]