# Generated by Django 4.2 on 2024-09-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_balance_alter_customuser_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Ученик'),
        ),
    ]
