# Generated by Django 5.1.1 on 2024-10-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_acne_proneness_profile_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skin_type',
        ),
        migrations.RemoveField(
            model_name='skincaregoal',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='skincondition',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='skin_conditions',
            field=models.ManyToManyField(to='accounts.skincondition'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skin_types',
            field=models.ManyToManyField(to='accounts.skintype'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skincare_goals',
            field=models.ManyToManyField(to='accounts.skincaregoal'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pics/default_pfp.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]