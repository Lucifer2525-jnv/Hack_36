# Generated by Django 3.2 on 2021-04-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'API',
                'verbose_name_plural': 'APIs',
            },
        ),
    ]
