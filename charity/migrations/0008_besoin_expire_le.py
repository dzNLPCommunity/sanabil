# Generated by Django 2.0.9 on 2019-03-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0007_auto_20190331_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='besoin',
            name='expire_le',
            field=models.DateField(blank=True, null=True),
        ),
    ]