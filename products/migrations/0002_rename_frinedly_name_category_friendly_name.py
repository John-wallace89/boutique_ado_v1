# Generated by Django 3.2.7 on 2021-10-02 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='frinedly_name',
            new_name='friendly_name',
        ),
    ]