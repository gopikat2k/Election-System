# Generated by Django 4.1.3 on 2023-03-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userregi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.TextField(max_length=30)),
                ('phonenumber', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=250)),
                ('uploadid', models.FileField(upload_to='pic')),
            ],
        ),
    ]
