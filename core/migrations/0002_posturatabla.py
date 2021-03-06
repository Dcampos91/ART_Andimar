# Generated by Django 3.2.8 on 2021-11-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosturaTabla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_conductor', models.IntegerField()),
                ('conductor', models.CharField(max_length=200)),
                ('auxiliar', models.CharField(max_length=200)),
                ('bus', models.IntegerField()),
                ('respuesta', models.TextField()),
            ],
            options={
                'db_table': 'posturatabla',
                'managed': True,
            },
        ),
    ]
