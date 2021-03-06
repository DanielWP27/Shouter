# Generated by Django 2.1.5 on 2019-01-22 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shout_text', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(verbose_name='date shouted')),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shouts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
