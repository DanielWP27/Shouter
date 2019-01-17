# Generated by Django 2.1.5 on 2019-01-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shout_text', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(verbose_name='date shouted')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(verbose_name='Date registered')),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
            ],
        ),
    ]
