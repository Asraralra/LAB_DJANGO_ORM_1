# Generated by Django 4.1.3 on 2022-11-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=2048)),
                ('Content', models.TextField()),
                ('is_published', models.BooleanField()),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
