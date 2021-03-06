# Generated by Django 2.2.16 on 2022-03-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20220327_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-year', 'id'), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
