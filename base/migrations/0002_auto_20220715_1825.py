# Generated by Django 3.2.12 on 2022-07-15 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['read']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='read',
        ),
    ]
