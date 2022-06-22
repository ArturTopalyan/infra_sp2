# Generated by Django 2.2.16 on 2022-03-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220322_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-year', 'rating'), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]