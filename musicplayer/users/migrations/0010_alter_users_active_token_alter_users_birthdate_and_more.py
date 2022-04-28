# Generated by Django 4.0.4 on 2022-04-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_users_active_token_alter_users_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='active_token',
            field=models.CharField(blank=True, default='918604', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='birthdate',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='fullname',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(default='MP6708329154', max_length=12),
        ),
    ]