# Generated by Django 5.0 on 2024-07-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PAGINA_WEB', '0006_alter_manga_titulo_alter_manga_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='Titulo',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
