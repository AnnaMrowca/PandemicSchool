# Generated by Django 3.2.1 on 2021-05-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(null=True, related_name='subjects', to='school.Student'),
        ),
    ]
