# Generated by Django 2.2.26 on 2022-05-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('patronomic', models.CharField(max_length=256)),
                ('date_brithday', models.DateField()),
            ],
        ),
    ]
