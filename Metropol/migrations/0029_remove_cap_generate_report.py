# Generated by Django 5.0.3 on 2024-05-29 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Metropol', '0028_rename_partner_reference_cap_application_reference_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cap',
            name='generate_report',
        ),
    ]