# Generated by Django 4.2.4 on 2024-01-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Metropol', '0016_alter_identitydetail_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BouCode',
            fields=[
                ('bou_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='identitydetail',
            old_name='user_image',
            new_name='image',
        ),
        migrations.CreateModel(
            name='BranchCode',
            fields=[
                ('branch_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('bou_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metropol.boucode')),
            ],
        ),
        migrations.AlterField(
            model_name='cap',
            name='partner_bou_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metropol.boucode'),
        ),
        migrations.AlterField(
            model_name='cap',
            name='partner_branch_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metropol.branchcode'),
        ),
    ]