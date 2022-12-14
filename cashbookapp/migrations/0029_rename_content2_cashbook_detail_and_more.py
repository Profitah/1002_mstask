# Generated by Django 4.0.4 on 2022-10-01 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0028_cashbook_content2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashbook',
            old_name='content2',
            new_name='detail',
        ),
        migrations.AlterField(
            model_name='cashbook',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='date published'),
        ),
    ]
