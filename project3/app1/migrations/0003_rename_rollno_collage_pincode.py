# Generated by Django 4.2.1 on 2023-05-23 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_collage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collage',
            old_name='rollno',
            new_name='Pincode',
        ),
    ]
