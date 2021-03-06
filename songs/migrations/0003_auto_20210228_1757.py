# Generated by Django 3.1.7 on 2021-02-28 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20210228_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='songs.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='band', to='songs.band'),
        ),
    ]
