# Generated by Django 2.2.2 on 2019-06-23 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hub', '0002_auto_20190621_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the question', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='applicants',
            field=models.ManyToManyField(blank=True, help_text='Applicants for the opportunity', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='opportunity',
            name='questions',
            field=models.ManyToManyField(blank=True, help_text='Additional questions related to the opportunity', to='hub.Question'),
        ),
    ]
