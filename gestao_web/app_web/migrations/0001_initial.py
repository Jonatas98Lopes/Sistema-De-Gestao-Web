# Generated by Django 4.1.7 on 2023-04-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entretenimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TimeField(max_length=255)),
                ('finalizado', models.BooleanField(default=False)),
                ('resenha', models.TextField(max_length=500)),
            ],
        ),
    ]