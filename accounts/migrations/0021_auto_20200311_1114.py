# Generated by Django 3.0.2 on 2020-03-11 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20191010_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Type down and/or select your course from the list', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Course'),
        ),
    ]