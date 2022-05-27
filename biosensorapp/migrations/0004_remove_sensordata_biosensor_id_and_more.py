# Generated by Django 4.0.4 on 2022-05-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biosensorapp', '0003_biosensortesttype_cholinesterasetype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='biosensor_id',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='cholinesterase_id',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='biosensor_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='cholinesterase_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
