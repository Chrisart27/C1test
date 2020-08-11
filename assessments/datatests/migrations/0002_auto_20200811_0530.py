# Generated by Django 3.1 on 2020-08-11 05:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datatests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='estimated_end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 11, 6, 30, 24, 344774, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='questionandanswer',
            name='selected_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datatests.answer'),
        ),
    ]
