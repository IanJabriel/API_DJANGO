# Generated by Django 5.0.2 on 2024-08-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_django', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ra',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
