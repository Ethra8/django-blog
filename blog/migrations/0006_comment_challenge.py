# Generated by Django 4.0 on 2024-04-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.FloatField(default=3.0),
        ),
    ]
