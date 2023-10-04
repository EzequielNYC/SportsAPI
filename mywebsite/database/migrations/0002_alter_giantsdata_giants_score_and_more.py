# Generated by Django 4.2.5 on 2023-10-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giantsdata',
            name='giants_score',
            field=models.IntegerField(blank=True, db_column='giants_score', null=True),
        ),
        migrations.AlterField(
            model_name='jetsdata',
            name='jets_score',
            field=models.IntegerField(blank=True, db_column='jets_score', null=True),
        ),
        migrations.AlterField(
            model_name='knicksdata',
            name='knicks_score',
            field=models.IntegerField(blank=True, db_column='knicks_score', null=True),
        ),
        migrations.AlterField(
            model_name='netsdata',
            name='nets_score',
            field=models.IntegerField(blank=True, db_column='nets_score', null=True),
        ),
        migrations.AlterField(
            model_name='yankeesdata',
            name='yankees_score',
            field=models.IntegerField(blank=True, db_column='yankees_score', null=True),
        ),
    ]