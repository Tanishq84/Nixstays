# Generated by Django 4.2.14 on 2024-08-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dp',
            field=models.ImageField(default='user_dp/user.jpg', upload_to='user_dp/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
