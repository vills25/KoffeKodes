# Generated by Django 5.2 on 2025-06-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_mymodel_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='description',
            new_name='address',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
