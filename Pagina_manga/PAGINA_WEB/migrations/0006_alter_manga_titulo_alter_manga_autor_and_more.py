# Generated by Django 5.0.6 on 2024-07-01 00:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PAGINA_WEB', '0005_manga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='Titulo',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='manga',
            name='autor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='manga',
            name='descripcion',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(30)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.CreateModel(
            name='capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_capitulo', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos', to='PAGINA_WEB.manga')),
            ],
        ),
    ]
