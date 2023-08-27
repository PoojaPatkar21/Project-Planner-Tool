# Generated by Django 4.2.4 on 2023-08-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('creationtime', models.DateTimeField(auto_now_add=True)),
                ('userdescription', models.CharField(max_length=250)),
            ],
        ),
    ]