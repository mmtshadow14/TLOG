# Generated by Django 5.1.3 on 2024-12-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_likerelation_postlikedid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likerelation',
            name='postLikedId',
            field=models.CharField(max_length=100),
        ),
    ]
