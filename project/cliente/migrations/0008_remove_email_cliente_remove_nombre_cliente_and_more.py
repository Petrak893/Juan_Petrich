# Generated by Django 5.0.4 on 2024-05-09 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_alter_cliente_email_alter_email_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='nombre',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.telefono'),
        ),
    ]
