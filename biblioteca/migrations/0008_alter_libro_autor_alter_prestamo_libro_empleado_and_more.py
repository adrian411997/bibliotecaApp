# Generated by Django 4.0 on 2023-06-19 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_alter_libro_autor_alter_prestamo_libro_empleado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor'),
        ),
        migrations.AlterField(
            model_name='prestamo_libro',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.empleado'),
        ),
        migrations.AlterField(
            model_name='prestamo_libro',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro'),
        ),
        migrations.AlterField(
            model_name='prestamo_libro',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.socio'),
        ),
    ]
