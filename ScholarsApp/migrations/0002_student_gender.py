# Generated by Django 4.2.3 on 2024-01-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=10),
            preserve_default=False,
        ),
    ]
