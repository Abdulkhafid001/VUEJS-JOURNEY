# Generated by Django 5.0.2 on 2024-03-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYBLOG', '0002_password_change_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password_change_request',
            name='mail_of_user',
            field=models.CharField(max_length=50),
        ),
    ]