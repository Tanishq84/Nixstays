# Generated by Django 4.2.14 on 2024-08-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_property_new_price_alter_property_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='food_icons/')),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='food_type',
        ),
        migrations.AddField(
            model_name='property',
            name='food_type',
            field=models.ManyToManyField(blank=True, related_name='properties', to='main.food'),
        ),
    ]
