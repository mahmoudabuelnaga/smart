# Generated by Django 2.1.3 on 2018-12-11 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptags', '0003_auto_20181203_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptags.Hashtags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
