# Generated by Django 4.0.6 on 2023-08-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='uploads/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('extension', models.CharField(max_length=10)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('file_size', models.BigIntegerField()),
            ],
        ),
    ]
