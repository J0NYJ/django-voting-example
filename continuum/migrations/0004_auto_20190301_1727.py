# Generated by Django 2.1.7 on 2019-03-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuum', '0003_user_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='votes',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
