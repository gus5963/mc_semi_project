# Generated by Django 3.1.3 on 2022-03-20 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourcomment',
            name='mbti_id',
        ),
        migrations.RemoveField(
            model_name='tourcomment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tourliked',
            name='like_user',
        ),
        migrations.RemoveField(
            model_name='tourliked',
            name='tour_id',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
        migrations.DeleteModel(
            name='TourComment',
        ),
        migrations.DeleteModel(
            name='TourLiked',
        ),
    ]