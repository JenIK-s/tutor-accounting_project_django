# Generated by Django 4.2 on 2024-09-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_remove_lessonaccounting_date_lessonaccounting_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='Баланс'),
        ),
    ]
